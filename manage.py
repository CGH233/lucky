#coding:utf-8
import sys
import os
from flask_script import Manager, Shell
from app import app


manager = Manager(app)

def make_shell_context():
    return dict(
        app = app
    )

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def createdb():
    db.create_all()


if __name__ == '__main__':
    manager.run()
