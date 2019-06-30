### Python Flask 系列 

From [网易云课堂](https://study.163.com/course/courseLearn.htm?courseId=1004091002#/learn/video?lessonId=1047958048&courseId=1004091002)

-------------

#### Contents

一、URLs 和 视图 [finish 8/12, next: 9]

二、jinja2 模板

三、SQL Alchemy 数据库 (用的是 MySQL)

四、Session 和 cookies 操作

五、知识点补充

六、项目实战

七、Flask 进阶

---------

#### 1. 学习目标

* 建立网站（前后端具备）

  ![imgs](/imgs/learnTarget.png)

  - 功能描述：登录/注册，发布问题，搜索，查看文档
  - 使用技术：前端 + 后端(MySQL) + Python 

#### 2. 基础知识

##### 2.1 Python 虚拟环境 (virtual env)

* 作用：因为Python框架 更新迭代速度太快了，有时候为了在同一台电脑上 能够运行一个框架的多个版本，各版本间又能不相互影响，就可以利用 `虚拟环境` 进行解决。

* 命令：

  ```shell
  # 安装虚拟环境
  $ pip install virtualenv
  # 创建虚拟环境
  $ virtualenv [virtualenv-name]
  # 激活
  $ [Unix] source [虚拟环境所在目录]/bin/activate
  $ [Windows] 直接进入虚拟环境所在目录，执行 activate 即可
  # 退出
  $ deactivate
  ```

##### 2.2 如何确定安装的 Flask 版本

* 安装好后，可用 python 查看版本号

  ```python
  import flask
  print(flask.__version__)
  ```

##### 2.3 Flask 程序 配置文件使用 (Config)

```python
# 把配置信息 存放在 配置文件config.py 中，然后主程序中导入配置即可！
import config
#主程序中导入
app = Flask(__name__)
app.config.from_object(config)
```

