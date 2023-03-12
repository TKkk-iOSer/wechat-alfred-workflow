
## wechat workflow for Alfred 3.0

![platform](https://img.shields.io/badge/platform-macos-lightgrey.svg)  ![language](https://img.shields.io/badge/language-python-blue.svg)
  ![release](https://img.shields.io/badge/release-v2.0-brightgreen.svg) 
 [![GitHub license](https://img.shields.io/github/license/TKkk-iOSer/wechat-workflow.svg)](https://github.com/TKkk-iOSer/wechat-workflow/blob/master/LICENSE)

一款让你不用打开微信就能聊天的`alfred workflow` 3.0

---

### 安装

* 下载 WeChat Plugin.alfredworkflow
* 安装requests：pip install requests
* 打开微信-菜单栏-微信小助手-小助手-开启alfred功能

### 功能

* 快速搜索微信好友、群聊
* 快捷发送消息 
* 快捷打开聊天窗口
* 支持搜索好友，匹配昵称、备注、微信号、国家、省份、市。
* 支持搜索群聊，匹配群聊昵称、群成员昵称、群成员备注名、群成员微信号
* 支持复制微信号、聊天内容(**2.0**)
* 聊天记录界面支持快捷打开微信聊天窗口(`Command + ↩︎`)(**2.0**)
* 支持预览长文本消息(`Command + L`)(**2.0**)
* 支持查看好友高清头像(`Command + Y`或者`shift`)(**2.0**)
* 支持预览视频、表情、图片、网址等消息(`Command + Y`或者`shift`)(**2.0**)
* 支持播放音频消息(直接选中音频消息回车)(**2.0**)
* 聊天记录显示发送时间(**2.0**)
* 默认打开最近聊天记录 & 获取聊天内容(**2.0**)
* 支持python3(**3.0**)

---

### Demo 演示

![alfred](./ScreenShots/alfred_search.gif)

~~懒得录制 gif 图了，自己看[功能](#功能) 或者 [使用](#使用) 或者 `Alfred` 中的提示~~

---

### 使用
* 下载该 [wechat-alfred-workflow](https://github.com/TKkk-iOSer/wechat-alfred-workflow/releases) & [WeChatPlugin-macOS](https://github.com/TKkk-iOSer/WeChatPlugin-MacOS)

* 启动`Alfred`，输入`wx`启动该 workflow。

* 启动`Alfred`，输入 `wx` + `空格` 键，快捷打开最近聊天会话。

![keyword](./ScreenShots/alfred_query.png)

* 搜索到好友，点击 `Enter` 键，并输入内容，则发送消息给好友(此时可看到下方30条最新聊天记录)。

![keyword](./ScreenShots/alfred_send.png)

* 搜索到好友(或者发送消息界面)，点击 `Command + Enter` 键，快捷打开聊天窗口。
* 选中好友(聊天记录)，点击 `Command + C` 键，复制好友微信号(聊天内容)。
* 选中聊天消息，`Command + L`预览长文本消息。
* 选中好友，`Command + Y`(`shift`)查看好友高清头像。
* 选中视频、表情、图片、网址等消息`Command + Y`(`shift`)预览非文本内容。
* 选中音频消息，在未输入发送内容时回车，可播放音频。

---

### 依赖

* [Alfred-Workflow](http://www.deanishe.net/alfred-workflow/index.html)

---

#### 听说你想请我喝下午茶？😏

<img src="http://upload-images.jianshu.io/upload_images/965383-cbc86dc1d75a6242.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" height="250" hspace="50"/>&nbsp;&nbsp;&nbsp;<img src="http://upload-images.jianshu.io/upload_images/965383-76a1c7c91b987e1a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" height="250" hspace="50"  />



