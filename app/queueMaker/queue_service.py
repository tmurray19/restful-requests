from datetime import datetime
from json import dump, load
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
        "dateCompleted": "TBA",
        "status": False,
        "otherInfo": "None"
    }
    try:
        # Open and write to file
        with open(join(app.config['DIR_LOCATION'], app.config['QUEUE_FOLDER'], proj_id + "_queue_status.json"), 'w') as outfile:
            dump(queue_info, outfile)
    
        print("Queue file written to {}".format(join(app.config['DIR_LOCATION'], app.config['QUEUE_FOLDER'], proj_id + "_queue_status.json")))
        return 1
    except Exception as e:
        print(e)
        print("An error has occured")
        return 0



def get_queue_status(proj_id):
    try:
        # Create The JSON File
        queue_loc = join(app.config['DIR_LOCATION'], app.config['QUEUE_FOLDER'], proj_id + "_queue_status.json")
        with open(queue_loc) as json_file:
            json_data = load(json_file)
            status = json_data['status']

    
    except Exception as e:
        status = str(e)

    if status == True:
        #logging.log("Project has been rendered")
        return 1
    else:
        #logging.log("Project has not been rendered")
        return 0