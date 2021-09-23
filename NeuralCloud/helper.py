import os
import json
import re
import time
import logging
from typing import Callable
from dataclasses import dataclass
from random import randint, uniform, gauss
from time import sleep, monotonic
from fractions import Fraction

import coloredlogs
import numpy as np

import config

from connector import auto_connect
from connector.ADBConnector import ADBConnector, ensure_adb_alive
from .frontend import DummyFrontend
from util.excutil import guard
from NeuralCloud import frontend
import logging

logger = logging.getLogger(__name__)


class NeuralCloudAutoHelper(object):
    def __init__(self, adb_host=None, device_connector=None, frontend=None):  # 当前绑定到的设备
        self.adb = None
        if adb_host is not None or device_connector is not None:
            self.connect_device(device_connector, adb_serial=adb_host)
        if frontend is None:
            frontend = DummyFrontend()
            if self.adb is None:
                self.connect_device(auto_connect())
        self.frontend = frontend
        self.frontend.attach(self)
        self.operation_time = []

        logger.debug("成功初始化模块")

    def connect_device(self, connector=None, *, adb_serial=None):
        if connector is not None:
            self.adb = connector
        elif adb_serial is not None:
            self.adb = ADBConnector(adb_serial)
        else:
            self.adb = None
            return
        self.viewport = self.adb.screen_size
        if self.adb.screenshot_rotate % 180:
            self.viewport = (self.viewport[1], self.viewport[0])
        if self.viewport[1] < 720 or Fraction(self.viewport[0], self.viewport[1]) < Fraction(16, 9):
            title = '设备当前分辨率（%dx%d）不符合要求' % (self.viewport[0], self.viewport[1])
            body = '需要宽高比等于或大于 16∶9，且渲染高度不小于 720。'
            details = None
            if Fraction(self.viewport[1], self.viewport[0]) >= Fraction(16, 9):
                body = '屏幕截图可能需要旋转，请尝试在 device-config 中指定旋转角度。'
                img = self.adb.screenshot()
                imgfile = os.path.join(config.SCREEN_SHOOT_SAVE_PATH,
                                       'orientation-diagnose-%s.png' % time.strftime("%Y%m%d-%H%M%S"))
                img.save(imgfile)
                import json
                details = '参考 %s 以更正 device-config.json[%s]["screenshot_rotate"]' % (
                    imgfile, json.dumps(self.adb.config_key))
            for msg in [title, body, details]:
                if msg is not None:
                    logger.warning(msg)
            frontend.alert(title, body, 'warn', details)
