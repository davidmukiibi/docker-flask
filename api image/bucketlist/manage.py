from flask_script import Manager # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from buckeT import db, app
from buckeT.database_models import User, BucketListItem, BucketList

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    """Creates database with tables"""
    db.create_all()

@manager.command
def drop_db():
    """Deletes database"""
    db.drop_all()

if __name__ == '__main__':
    manager.run()