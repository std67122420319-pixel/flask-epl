from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///epl.db'
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from epl import routes, models