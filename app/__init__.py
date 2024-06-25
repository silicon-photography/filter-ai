import os
import sys
import flask


def create_app():
    app = flask.Flask(__name__)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route("/")
    def hello():
        return "Hello";
    
    return app