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

-----------

#### SQLAlchemy ORM 模型

* 多对多关系映射（加入一张组合表[中间表] 进行关联）

  * 注意：中间表 不能通过定义 class类 的方式进行实现，而必须使用 `db.Table` 方式进行实现！
  * 同时中间表中 需要添加相应的关联关系 `db.relationship`，不然多对多关系将无法建立！

  ```sql
  # 创建 article 表
  create table article (
  	id int primary key autoincrement,
    title text not null
  );
  
  # 创建 tag 表
  create table tag (
    id int primary key autoincrement,
    name varchar(50) not null
  );
  
  # 多对多关系映射表 (每一篇文章可以对应多个标签，每个标签也可以对应多篇文章)
  create table article_tag (
  	article_id int,
  	tag_id int,
  	primary key('article_id', 'tag_id'),
  	foreign key 'article_id' references 'article.id',
  	foreign key 'tag_id' references 'tag.id'
  );
  ```

  对应于 SQLAlchemy 框架，用类来代替关系

  ```python
  class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    # 两张原本独立的表 之间建立关联 (relationship)
    tags = db.relationship('Tag', secondary=article_tag, backref=db.backref('articles'))
    
  class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    
  # 重点：将上面两张表进行 多对多映射 的关键
  article_tag = db.Table('article_tag', 
    db.Column('article_id', db.Interger, db.ForeignKey('article.id'), primary_key=True)
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
  )
  ```

  * 使用方法：

    ```python
    调用 db.relationship 实现多对多关系映射
    article1.tags.append(tag1)
    article1.tags.append(tag2)
    
    article2.tags.append(tag1)
    article2.tags.append(tag2)
    ```

----

#### Models 与 后台逻辑代码 分离

1. 从后台Python代码中 将Models分离出来的主要目的是：为了结构更加清晰，提高代码可维护性！

2. 分离models的难点在于：解决循环引用

   * 解决方法：

   ```python
   # 把 db 的创建 与 初始化 分离
   exts.py
   	db = SQLAlchemy()
   ----
   model.py
   	from exts.py import db
     class Article(db.Model): xxx
   ----
   main.py
   	from flask import Flask
     from exts import db
     from model import Article
     import config
     
   	app = Flask(__name__)
     app.config.from_object(config)
   	db.init_app(app)
     
     # 手动将 app 加入到 上下文管理器，以创建数据库表
     with app.app_context():
       db.create_all()
   ```

-----

#### 数据库 迁移 (flask-migrate)

1. 使用场景：当数据库表中已经存在数据了，再添加新的字段，表无法通过`db.create_all()`命令进行修改，这个时候当然也不可能直接删除原先的表 然后重新创建；

2. 这个时候 **数据库迁移** 就派上用场了，它会创建新表，同时将 原表中的数据 全部迁移到这张新表中！保证数据不丢失！

   * 使用方法

   ```python
   manage.py
   
   from flask_script import Manager
   from flask_migrate import Migrate, MigrateCommand 
   # MigrateCommand 中包含了所有与数据库迁移相关的 命令(init/migrate/upgrade)，调用 flask_script 即可执行这些命令 完成数据库迁移
   from migrate_demo import app
   from exts import db
   
   from models import Article
   
   manager = Manager(app)
   migrate = Migrate(app, db)
   manager.add_command('db', MigrateCommand)
   
   if __name__ == '__main__':
     manager.run()
   ```

   * 注意：这里最合适的方式是：结合使用 flask-migrate && flask-script 两大插件！

3. 数据库表创建 与 数据迁移 命令

   ```shell
   # 表初始化(表创建)
   $ python manage.py db init 
   
   # 数据库中 数据迁移
   $ python manage.py db migrate
   $ python manage.py db upgrade
   ```

   