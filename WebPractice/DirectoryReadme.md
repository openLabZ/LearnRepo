### 实战项目 项目说明

----

#### 1. 目录结构 及 文件用途

```
WebPractice git:(master) ✗ tree
.
├── DirectoryReadme.md
├── config.py   # 配置 文件
├── exts.py     # db 分离 (便于拆分models)
├── manage.py   # 数据迁移
├── models.py   # 模型文件
├── static      
├── templates
└── web.py      # 项目主文件

```

#### 遗留问题

1. 怎么把 web.py 与 main.py 这两个文件解耦的？
（直接分开 会导致 web.py 在运行时 app上未注册任何url！导致 404 Not-Found! ）
（解决方法：使用 app.register_blueprint 方法 注册app函数，实现解耦！）

```python
>>> web.py
from controllers import *
from models import db

app = Flask(__name__)
config_blueprint(app)
app.config.from_object(database_conf)
db.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8090")
    
>>> controller > __init__.py

from controllers.main import *

DEFAULT_BLUEPRINT = [
    [main, '']
]

def config_blueprint(app):
    for each in DEFAULT_BLUEPRINT:
        app.register_blueprint(each[0], url_prefix=each[1])
        
        
>>> controller > main.py
main = Blueprint('main', __name__)

def func():
    pass
```

2. 对 className 属性的增加删除与修改
https://blog.csdn.net/Dorui/article/details/78313014

3. Bootstrap 导航栏 active 属性 (失效原因：active 没加对地方！)
https://cloud.tencent.com/developer/ask/109921

    [失效原因] active 类属性 需要加在 \<a\> 标签上，而不要加在 \<li\> 标签上！
    ```html
    <div style="float: left; ">
        <ul class="nav nav-pills flex-column">
            <li class="nav-item leftNavLi">
                <a class="nav-link" href="#">Link-1</a>
            </li>
            <li class="nav-item leftNavLi ">
                <a class="nav-link active" href="#">Link-2</a>
            </li>
            <li class="nav-item leftNavLi">
                <a class="nav-link" href="#">Link-3</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Link-4</a>
            </li>
        </ul>
    </div>
    ``` 

----

#### PNFWeb 遗留问题

1. js 动态添加 class="active" 属性，效果总是 “日志闪现”, active不生效
（定位原因：PNFWeb中 每点击一次nav导航元素，就会在后台调用 render_templates() 重新渲染 给用户提供一个全新的页面）
（在新页面中，原先动态添加的 active 此时已经被覆盖了，所以新页面展现出来的效果就是 上个页面的日志-瞬间消失了 && 上个页面的active属性对本页面不生效）！

