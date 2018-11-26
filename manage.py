from app import create_app,db
from app.models import User
from app.models import User,Role
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand


app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)