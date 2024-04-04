# 地图上传计划

这个项目是一个允许用户提交地图信息的应用. 地图信息包括地图名称、地图URL、URL提取码和地图类别. 提交的信息会根据地图名称检查重复，然后保存到一个JSON文件中. 如果找到重复的地图名称，提交将被拒绝，并返回一个错误消息. 如果提交成功，将返回一个成功消息. 

应用的后端使用 Python 和 Flask 框架构建. 前端使用 Html 和 JavaScript 构建. 

## 安装

要运行此项目，您需要在您的机器上安装 Python. 您可以从官方网站下载 Python: https://www.python.org/downloads/

安装 Python 后，您需要安装必要的 Python 库. 您可以通过在终端运行以下命令来实现: 

```bash
pip install flask flask_cors
```

此命令安装了Flask(一个用Python编写的微型网络框架)和Flask-CORS(一个处理跨源资源共享(CORS)的Flask扩展，使跨源AJAX成为可能). 

## 使用

要启动服务器，导航到终端的项目目录，然后运行以下命令: 

```bash
python main.py
```

服务器将在 5000 端口启动. 您可以通过打开网络浏览器并导航到 http://127.0.0.1:5000/ 来访问应用. 

## 贡献

欢迎贡献. 请随时提交拉取请求或打开问题. 

## 许可

此项目根据MIT许可条款获得许可. 