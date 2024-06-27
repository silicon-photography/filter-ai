from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route("/")
    def hello():
        return "Hello"

    from .blueprints import calendar
    app.register_blueprint(calendar.bp, url_prefix='/calendar')
    
    return app
