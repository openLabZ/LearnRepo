### Flask Web 开发拓展知识

----

#### 1. GET 请求 & POST 请求

* 怎么看网站用的 GET/POST 请求的具体运行情况？

  Google浏览器，右击 -> "检查" (进入开发者模式) -> “Network” (会展现所有发送到服务器端的请求情况)

* Get 和 Post 请求 获取请求参数

  ![image-20190703012232724](/imgs/image-20190703012232724.png)

#### 2. Flask 中的 g 属性 (线程隔离的全局g对象(global对象))

* from flask import Flask, g

* g 对象 专门用于保存用户的数据，g 对象 在一次请求中所有代码都可以共享使用！