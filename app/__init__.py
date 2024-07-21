from flask import Flask, jsonify
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

if __name__ == '__main__':
    app = create_app()
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error: {e}")
