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
