from datetime import datetime
from json import dump
from os.path import join
from app import app

def create_queue(proj_id):
    # Define data points
    """
    ID: int --> Project ID
    dateRequested: String --> Exact time requested at
    dateCompleted: String --> Time video was written to file
    status: Bool --> True for completed, False for not
    otherInfo: String --> Any error messages
    """
    # Create json info
    queue_info = {
        "id": proj_id,
        "dateRequested": datetime.now().strftime("%d-%b-%Y (%H:%M:%S)"),
        "dateCompleted": "",
        "status": False,
        "otherInfo": ""
    }
    # Open and write to file
    with open(join(app.config['DIR_LOCATION'], app.config['QUEUE_FOLDER'], proj_id + "_queue_status.json"), 'w') as outfile:
        dump(queue_info, outfile)
    
    print("Queue file written to {}".format(join(app.config['DIR_LOCATION'], app.config['QUEUE_FOLDER'], proj_id + "_queue_status.json")))
