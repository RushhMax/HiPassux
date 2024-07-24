from app.controllers import user_controller, post_controllers, reaction_controllers, message_controllers, comment_controllers

def init_routes(app):
    app.register_blueprint(user_controller.bp)
    app.register_blueprint(post_controllers.bp)
    app.register_blueprint(reaction_controllers.bp)
    app.register_blueprint(message_controllers.bp)
    app.register_blueprint(comment_controllers.bp)
    # Test route Blueprint