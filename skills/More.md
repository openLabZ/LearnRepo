### Flask 常用插件介绍

----

1. Flask Script

   作用：可以让我们 通过 命令行 的形式来操作Flask，比如：通过命令运行服务器，通过命令一键设置数据库，通过命令启动定时任务等等！



### Python & Pip 常用命令

----

1. 如何确定我当前所处的 Python环境中，pip install 了哪些工具呢？

   使用命令：`pip list` 进行查看！



#### MAC 安装 MySQL 8.0 以上版本时

* 请注意：

  ```mysql
  # 手动 创建 数据库表
  mysql> create database webflask charset utf8;
  
  # 为root用户 重置密码
  mysql> alter user 'root'@'localhost' identified by 'Root@123';
  Query OK, 0 rows affected (0.00 sec)
  ```

  * mysql 8.0以上 密码策略：限制 **必须要大小写加数字特殊符号**！
  * 如果 密码设置的不符合要求，就会设置失败，就会导致你无法进入！

* 实战注意：

  ```shell
  # 依赖插件有：Flask-SQLAlchemy / Flask-Script / Flask-Migrate
  $ sudo pip3 install flask_sqlalchemy
  $ sudo pip3 install flask_script
  $ sudo pip3 install flask_migrate
  ```

  