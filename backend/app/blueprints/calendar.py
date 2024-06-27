from flask import Blueprint, render_template
from typing import Dict
from datetime import datetime

bp = Blueprint('calendar', __name__) # create a blueprint for the calendar feature

def validate_event(input_data: Dict[str, any]):
    fields = ["title", "description", "start_time", "end_time", "event_type", "attendees"] # add required fields for form
    
    # Check to see if the user input from the form has all fields
    for field in fields:
        if field not in input_data:
            return False
    
    # Convert the date strings into a date object
    try:
        datetime.strptime(input_data['start_time'], '%Y-%m-%dT%H:%M')
        datetime.strptime(input_data['end_time'], '%Y-%m-%dT%H:%M')
        
    except ValueError:
        return False
    
    return True
        

@bp.route('/add_event', methods=['GET'])
def add_event():
    return "add_event";