# from flask import Flask
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///epl.db'
# app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


# from epl import routes, models

from flask import Flask, app
from epl.extensions import db, migrate
from epl.core.reutes import core_bp
from epl.models import Club, Player
from epl.clubs.routes import club_bp
from epl.players.reutes import player_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///epl.db'
    app.secret_key = b'asjdlkdjkasdjkasjdlkjasdjasdlk'

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(core_bp, url_prefix='/')
    app.register_blueprint(club_bp, url_prefix='/clubs')
    app.register_blueprint(player_bp, url_prefix='/players')

    return app