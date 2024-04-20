from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

# https://www.youtube.com/watch?v=v6b4tggM7M0&list=PLe4mIUXfbIqaLWrzsSDQAAK3_NQB1jBZZ&index=5
'''
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
'''

app = Flask(__name__,template_folder='templates', static_folder='static')
app.config.from_object(Config)

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()
    Migrate(app, db).init_app(app, db)
