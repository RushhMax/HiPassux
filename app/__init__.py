from flask import Flask
from app.extensions import db, migrate
from app.routes import init_routes
from app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['DEBUG'] = True

    db.init_app(app)
    migrate.init_app(app, db)
    
    init_routes(app)
    
    return app
app = create_app()