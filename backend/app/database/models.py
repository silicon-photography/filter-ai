from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Time

db = SQLAlchemy()

class CalendarDev(db.Model):
    # Define table name
    __tablename__ = "calendar_dev"
    
    # Define schema
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    start_time = db.Column(Time, nullable=False)
    end_time = db.Column(Time, nullable=False)
    event_type = db.Column(db.String(64), nullable=False)
    attendees = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    location = db.Column(db.String(256), nullable=False)

class CalendarTest(db.Model):
    # Define table name
    __tablename__ = "calendar_test"
    
    # Define schema
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    start_time = db.Column(Time, nullable=False)
    end_time = db.Column(Time, nullable=False)
    event_type = db.Column(db.String(64), nullable=False)
    attendees = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    location = db.Column(db.String(256), nullable=False)