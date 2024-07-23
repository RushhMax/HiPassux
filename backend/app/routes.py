from app.controllers import user_controller

def init_routes(app):
    app.register_blueprint(user_controller.bp)
    # Test route Blueprint