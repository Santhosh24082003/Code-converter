from .conversion_routes import conversion_blueprint

def init_routes(app):
    app.register_blueprint(conversion_blueprint)
