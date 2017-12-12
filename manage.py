from movies import app, db
from flask_script import Manager,prompt_bool

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    print('initialize')



@manager.command
def dropdb():
    if prompt_bool('are you sure?'):
        db.drop_all()
        print('dropped db')




if __name__=='__main__':
    manager.run()