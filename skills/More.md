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
  
  # 还得安装 SQLAlchemy 与 MySQL 之间连接的驱动 
  ❌ (mysql-python 不支持 python3)
  ✅ mysql-connector
  * Mac / 类 Unix
  $sudo pip3 install mysql-connector
  * Windows
  $pip install mysql-connector-python
  ```

  * [Python操作MySQL之SQLAlchemy](https://www.cnblogs.com/ccorz/p/5711955.html)

    ```
    [MySQL-Python]
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
    
    [MySQL-Connector]
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
    
    [pymysql]
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
        
    [cx_Oracle]
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
    ```

  * 连接过程中报错解决：

    ```
    问题现象：Can't connect to mysql server on '127.0.0.1' (61) - (MacOS)
    ERROR 2003 (HY000) Can't connect to MySQL server on '<remote-ip>' (61)
    
    解决方法：重启 Mysql Server
    
    1. 命令行中停止mysql服务：
    sudo /usr/local/mysql/bin/mysqladmin -u root -proot shutdown
    2. 系统偏好设置 > MySQL
    Start MySQL Server
    ```

    
