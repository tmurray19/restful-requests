from datetime import datetime
from json import dump, load
from os.path import join
from app import app
import logging
from app.fileShare import null_link

def create_queue(proj_id, compressed_render, chunk_render):
    # Null link in database
    null_status = null_link.null_project_link(proj_id)
    logging.debug("Null status: {}".format(null_status))

    # Define data points
    """
    ID: int --> Project ID
    dateRequested: String --> Exact time requested at
    dateCompleted: String --> Time video was written to file
    status: Bool --> True for completed, False for not
    otherInfo: String --> Any error messages
    """
    compress_bool = True if compressed_render==1 else False
    chunk_book = True if chunk_render==1 else False
    # Create json info
    queue_info = {
        "id": proj_id,
        "dateRequested": datetime.now().strftime("%d-%b-%Y (%H:%M:%S)"),
        "dateCompleted": "TBA",
        "status": False,
        "compressedRender": compress_bool,
        "chunkRender": chunk_book,
        "otherInfo": "None"
    }
    try:
        # Open and write to file
        with open(join(app.config['BASE_DIR'], app.config['QUEUE_FOLDER'], proj_id + "_queue_status.json"), 'w') as outfile:
            dump(queue_info, outfile)
    
        logging.debug("Queue file written to {}".format(join(app.config['BASE_DIR'], app.config['QUEUE_FOLDER'], proj_id + "_queue_status.json")))
        
        return 1
    except Exception as e:
        logging.error("An Exception has occured:")
        logging.error(e)
        return 0



def get_queue_status(proj_id):
    try:
        # Create The JSON File
        queue_loc = join(app.config['BASE_DIR'], app.config['QUEUE_FOLDER'], proj_id + "_queue_status.json")
        with open(queue_loc) as json_file:
            json_data = load(json_file)
            #status = json_data['status']
            logging.debug("File render status: {}".format(json_data['correctlyRendered']))
            logging.debug("Info: {}".format(json_data['otherInfo']))
            return json_data['correctlyRendered']

    
    except Exception as e:
        logging.debug(e)
        return -1

    """    
    if status == True:
        logging.debug("Project has been rendered")
        return 1
    else:
        logging.debug("Project has not been rendered")
        return 0"""