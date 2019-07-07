### Flask Web 开发拓展知识

----

#### 1. GET 请求 & POST 请求

* 怎么看网站用的 GET/POST 请求的具体运行情况？

  Google浏览器，右击 -> "检查" (进入开发者模式) -> “Network” (会展现所有发送到服务器端的请求情况)

* Get 和 Post 请求 获取请求参数

  ![image-20190703012232724](/imgs/image-20190703012232724.png)


* <font color="red">GET 请求 和 POST 请求的区别</font>
  - **GET 请求**：只是从 服务器 获取数据，不会对服务器本身产生任何影响！
    
    - 传参方式：在URL中 以`?`的形式 制定 key 和 value 进行 参数传递！
    
      ```python
      # 后台获取：
      data = request.args.get('key')
      ```
    
  - **POST 请求**：需要对服务器进行改动，
    
    - 比如 注册时在数据库表中 添加新行，登录时在服务器端记录Session 等场景，都对服务器本身产生了影响，此时发送的就是 POST请求！
    
    - 传参方式：涉及服务器的内容 绝不可以URL的方式直接显式的传递参数，而是应该使用`Form-Data`对表单数据进行隐式传递！
    
      ```python
      # 后台获取：
      username = request.form.get('username')
      password = request.form.get('password')
      ```
    
#### 2. Python Flask 中 怎么发起 POST 请求？

1. 在 前端页面html 中，明确此次提交为 POST 类型，指明 `method="POST"`，同时要指明`action='xxx'` 代表当我们提交表单时，表单数据需要推送到哪个页面上去；

2. 在 服务器端 处理方法中，明确声明可以处理 POST类型请求，同时利用 `request`  正确识别POST请求，并进行业务逻辑处理！

   ```python
   前端：
   <form class="xx" method="POST">
   <table>
   	<tr><td>用户名</td><td><input type="text" name="username" /></td></tr>
   	<tr><td>密码</td><td><input type="text" name="password" /></td></tr>
   </table>
   </form>
   
   后台 Server：
   @app.route('/login/', methods=['GET', 'POST'])
   def login():
     if request.method == 'GET':
         return render_template('login.html')
     else: # request.method = 'POST'
         pass
   ```

   

#### 3. Flask 中的 g 属性 (线程隔离的全局g对象(global对象))

* from flask import Flask, g

* g 对象 专门用于保存用户的数据，g 对象 在一次请求中所有代码都可以共享使用！

#### 4. 钩子函数使用

1. before_request

   ```python
   @app.before_request
   def my_request():
     # 执行 request请求前 一定会执行的代码
     # 通常可用于设置全局 g对象
   ```

   - before_request：顾名思义，它是在之前所有 request 请求之前 都会被调用的一个函数！

2. context_processor 上下文处理器 (环境统一执行器)

   ```python
   @app.context_processor
   def my_processor():
     user = session.get('user')
     if user:
       return {'user':user}
     else:
       return {}
     
   # 解释：
   # 以 返回字典 的方式，向全局上下文(全局环境)中 传递 关键信息！
   在这个函数中返回的 字典，在 所有页面 中均可用！
   # 以备全局各个页面 可方便获取并利用该 字典数据！
   ```

   