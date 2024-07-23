from app.api.user_api import user_api

def init_api_routes(app):
    app.register_blueprint(user_api)
