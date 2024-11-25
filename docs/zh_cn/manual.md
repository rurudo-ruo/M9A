# M9A 使用指南

## 开始前必读

M9A 支持在多种主流模拟器环境下自动执行游戏任务，以达到解放双手的目的。在开始之前，请确保正确下载、安装并配置 M9A。

### 关于下载

- **M9A 唯一官方发布页**：请访问 GitHub release 选择适合您平台架构的版本进行下载。

### 关于安装

- M9A 为便携式包体，下载后无需安装，但需要解压缩才能运行。请在文件管理器中找到刚下载的压缩包，并将其解压至您熟悉的目录，解压完成后即可开始使用！

### 如何启动

- M9A 支持两种启动方式：`MFAWPF.exe` 和 `MaaPiCli.exe`。前者为用户友好的图形界面，后者为命令行界面，二者功能一致。
- **建议**：一般用户请选择 `MFAWPF.exe` 启动。小贴士：可以将 `MFAWPF.exe` 创建桌面快捷方式，方便下次启动时使用。
- 以下教程将以 `MFAWPF.exe` 为基础进行介绍，技术用户可自行尝试 `MaaPiCli.exe`。

### 关于更新

- M9A 将不定期修复 bug 并适配新功能，请定期更新以获取最新支持。
- 启动时，M9A 将尝试连接 GitHub 检查更新，若检测到更新，将在软件右上角弹窗提示。如果您的设备当前无法连接 GitHub，将不会有更新提示，请访问 GitHub release 手动检查是否有新版本发布。
- 目前 M9A 无法在软件内直接更新，若有更新，请访问 GitHub 发布页下载最新压缩包，解压至原安装目录并覆盖即可完成更新。
- **推荐**：更新前删除原目录下除 `config` 文件夹以外的所有文件，以避免跨版本更新带来的问题。

## 功能介绍

在设置得当的情况下，M9A 可以实现一键解放双手。启动 M9A 后，它将自动启动模拟器中的 1999 并开始执行任务，包括：

- 收集荒原资源
- 刷新每日意志解析
- 清空体力
- 领取奖励
- 自动退出游戏

此外，M9A 还支持自动推图（不支持主线）和自动刷肉鸽奖励等功能。更多功能敬请期待！

想要实现以上效果吗？请参照以下内容对 M9A 进行配置。

## 模拟器配置

- *监修中*

### 软件设置

1. 首次进入模拟器后，请点击刷新图标搜索模拟器。该过程会自动完成，完成后将在软件右上角弹窗通知。请下拉选择安装了 1999 的模拟器。
2. 点击设置图标，软件中间将显示 M9A 普通设置，您也可以点击高级设置切换至高级设置。

#### 普通设置

- **资源**：默认为官服。如果您正在游玩其他服务器版本的 1999，请在资源一栏选择正确的区服。
- **捕获方式**：一般无需更改，M9A 将自动选择最快的截图方式。
- **触控模式**：一般无需更改，M9A 将自动选择最快的触控模式。
- **颜色主题**
- **语言（Language）**

#### 高级设置

- **启动后操作**：默认为无。如果您需要 M9A 启动后直接开始执行任务，请选择执行脚本。
- **结束后操作**：默认为无。如果您需要执行完所有脚本之后关闭 MFA、关闭模拟器或是关闭电脑等，请选择符合的选项。
- **启动 MFA 后启动模拟器**：默认不勾选。如果您需要 M9A 启动后自动启动模拟器，请勾选并在“模拟器路径”一栏填写正确的路径。
- **模拟器路径**：默认为空。如果您需要启动后自动启动模拟器，请在此填入正确的路径。
- **等待模拟器启动时间（秒）**
- **启动参数**
- **记住连结**
- **启用 GPU 加速**：默认勾选。如果您遇到肉鸽报错的问题，请取消勾选。

### 任务列表

软件左侧为任务列表栏目，以下将详细对该部分进行讲解：

- **启动游戏**：勾选后，M9A 将尝试启动 1999。
- **收取荒原**：勾选后，M9A 将尝试进入荒原。
- **每日心相（意志解析）**
- **自动深眠**
- **常规作战**
- **活动刷取**
- **领取奖励**
- **轶事派遣**
- **雨中悬想**
- **关闭游戏**
- **推图模式**
- **局外演绎**
- ...

## 常见问题

- 若提示“应用程序错误”，请访问 vc_redist.x64.exe 更新运行库。
- 更新后如报错，请删除原文件夹并重新解压安装。
- 如果肉鸽报错，请尝试在高级设置中关闭启用 GPU 加速。
- ...

---
