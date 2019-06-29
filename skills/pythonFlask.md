## Python Web Flask 框架

* [使用指南 —— 关于 Flask](http://docs.jinkan.org/docs/flask/index.html)
* [Python Flask 基础](https://study.163.com/course/introduction.htm?courseId=1004091002#/courseDetail?tab=1) from 网易云课堂
* [Flask Web 实战开发教程](https://blog.csdn.net/zhjm07054115/article/details/79743207) —— 打造上线可用的多媒体网站 from 优酷
* [Flask Web项目 部署后](https://blog.csdn.net/feit2417/article/details/80837297)
  - 前端（templates, static）
  - 后端（apps）


* 一个最简单的 Flask Web 程序

  ```python
  from flask import Flask
  app = Flask(__name__)
  
  @app.route('/')
  def hello_flask():
  	return 'Hello Flask!'
  
  if __name__ == '__main__':
  	app.run(host='127.0.0.1', port='8080')
  ```

  - app.run() 默认会映射到 127.0.0.1:5000 (本地 port 5000 访问)
  - app.run(host, port) 可以指定映射主机及端口号
  - `app.run(host='0.0.0.0')` 使你的服务器公开可用，它会让操作系统监听所有公网IP

* 启用 Flask <font color="red">调试模式</font>（每次修改不用重启服务，直接刷新即可，赞）

  ```python
  app.debug = True
  app.run()
  或者
  app.run(debug=True)
  ```

  * 使你不用每次修改都手动重启服务，**启用了调试模式后，服务器会在代码修改后自动重新载入**，并在发生错误时提供一个相当有用的调试器。
  
  --------
