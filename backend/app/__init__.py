from flask import Flask, jsonify
from app.extensions import db, migrate
from app.routes import init_routes
from app.config import Config
from app.api_routes import init_api_routes #importante tienes que poner el directorio del modelo de tu tabla
from app.domain.entities.user import db  #importante tienes que poner el directorio del modelo de tu tabla



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
<<<<<<< HEAD
    app.secret_key = 'mi_clave_secreta_super_segura'
=======

>>>>>>> origin/desarrollo
    db.init_app(app)
    migrate.init_app(app, db)
    
    init_routes(app)
    init_api_routes(app)

    return app




if __name__ == '__main__':
    app = create_app()
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error: {e}")