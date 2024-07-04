from flask import Flask
import os
import config

from database.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevConfig)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
        
    return app

app = create_app() # instantiate the app
db.init_app(app=app) # instantiate the db


# create the tables defined in model.py
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)