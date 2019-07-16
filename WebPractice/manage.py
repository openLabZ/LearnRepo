# -*- encoding: utf-8 -*-

# 用于 结合 flask-script & flask-migrate 进行数据库迁移

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from web import app
from controllers import db

manager = Manager(app)

# 使用 Migrate 绑定 app 和 db
migrate = Migrate(app, db)
# 将迁移命令加入到 Manager 中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
