### 网站开发之 Cookie & Session

----

1. Cookie 和 Session 是一对 孪生兄弟

   ![image-20190702235313060](/imgs/image-20190702235313060.png)

   * Cookie 存储在用户浏览器中 (为了信息安全，cookie中不直接存储用户信息，而是存储对应于该用户在服务器端放置的 Session的 session-id )
   * Session 经过加密存储在服务器中 (为了信息安全，session 中所存储的用户信息是经过加密的，同时还可为每个session设置过期时间，用户太久不访问后 session 自动失效，下次再登录用户需要重新认证)

2. Flask 中的 Session 机制

   ![image-20190703000451226](/imgs/image-20190703000451226.png)

3. Flask 中 Session 的使用

   ```python
   from flask import Flask, session
   
   app = Flask(__name__)
   # 随机 生成24位 盐值，用于加密
   app.config['SECERT_KEY'] = os.urandom(24)
   
   # 操作 Session 就像操作 Python字典 一样
   session['username'] = 'zcc'
   session.get('username')
   
   session.pop('username') / del session['username']
   session.clear()
   ```

   ![image-20190703003534484](/imgs/image-20190703003534484.png)

4. 设置 Session 过期时间

   * 如果默认没有设置，则默认过期时间为 `浏览器关闭后 删除`；

   * 如果开启了 session 的 **permanent** 属性，则过期时间默认会被修改为 31 天；

   * 如果开启了 permanent 属性，同时指定了 过期时间长度，则过期时间会被修改为你自己设置的时长！

     ```python
     app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelay(days=7)
     ```

     

