# Neural Cloud Auto Helper
> 云图计划辅助脚本 （开发中）

##

## 0x01 运行须知

### OCR 依赖

目前可以使用 tesseract（需另行安装）、Windows OCR（需要 Windows 10 简体中文系统或语言包）和百度 OCR API，请参阅 [OCR 安装说明](https://github.com/ninthDevilHAUNSTER/ArknightsAutoHelper/wiki/OCR-%E5%AE%89%E8%A3%85%E8%AF%B4%E6%98%8E)。



###  **环境与分辨率**
> 💡 由于游戏内文字渲染机制问题，分辨率过低可能影响识别效果，建议分辨率高度 1080 或以上。

大部分功能可以自适应分辨率（宽高比不小于 16:9，即`宽度≥高度×16/9`）

#### 常见问题

##### ADB server 相关

* 部分模拟器（如 MuMu、BlueStacks）需要自行启动 ADB server。
* 部分模拟器（如 MuMu）不使用标准模拟器 ADB 端口，ADB server 无法自动探测，需要另行 adb connect。
* 部分模拟器（如夜神）会频繁使用自带的旧版本 ADB 挤掉用户自行启动的新版 ADB。

#### **日志说明**
运行日志（文本）采用```import logging```在log目录下生成**NeuralCloudAutoHelper.log**推荐用Excel打开，分割符号为“!”

相关配置文件在```config```目录下的**logging.yaml**，由于过于复杂 ~~其实也没确定理解的对不对~~ 这里请自行研究，欢迎讨论

日志目前启动按照时间自动备份功能，间隔为一天一次，保留最多7份。

图像识别日志为 `log/*.html`，相应识别模块初始化时会清空原有内容。

多开时日志文件名会出现实例 ID，如 `NeuralCloudAutoHelper.1.log`。


## 0x08 自定义开发与TODO

### TODO

招募开发者。
