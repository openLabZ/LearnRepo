### ORM框架 之 flask_sqlalchemy

------

1. ORM 是什么？

   ORM = Object Relation Mapping

   代表的就是 对象与关系型数据库表之间关系 的映射！

2. ORM 可以用来做什么？

   - 对于 传统关系型数据库，我们要想使用 必须得写 sql语句 才能够对之进行管理；
   - 在 Web 项目中，为了让项目与 数据库 解耦，不用直接操作关系，我们定义了ORM！
   - ORM 可以 让我们 操作数据库就行是操作 类 一样！不需要通过sql语句 管理数据库，而是通过 <u>对象和方法</u> 达到管理数据库的目的！

   举例：

   ```
   传统关系型数据库：
   id = 1, title = "abc", content = "ddffeegg"
   操作：增删改查
   insert into ARTICLE values (1, "abc", "ddffeegg");
   delete from ARTICLE where id = 1;
   update ARTICLE set title = "new" where id = 1;
   select id, title, content from ARTICLE;
   
   ---------------
   
   使用 ORM ：
   O: Object (类和对象)
   R: Relation (关系数据库)
   M: Mapping (映射)
   
   类和对象：
   class Article(Model):
   	id = Int()
   	title = String()
   	content = Text()
   	
   article1 = Article(id=1, title="abc", content="ddffeegg")
   
   操作：增删改查
   add(article1)
   article1.title="bbb"
   update(article1)
   delete(article1)
   ```

3. 使用 ORM 的好处：

   - 使得 我们操纵数据库 可以变得更简单直接 (数据库操作 就像 Python类 一样)

4. ORM 安装：`pip install flask-sqlalchemy`