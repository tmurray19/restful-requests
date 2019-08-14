import os


# Config file
class Config(object):
    # Secret key used for verification
    SECRET_KEY = os.environ.get('SECRET_KEY') or "WgnYVzwgwF7Alu1B3DehuO-C-QoKcBitsHqpiFi1cRE"
    BASE_DIR = os.environ.get('BASE_DIR') or "/mnt/csae48d5df47deax41bcxbaa"
    #BASE_DIR = os.environ.get('BASE_DIR') or "N:/project"
    VIDS_LOCATION = os.environ.get('VIDS_LOCATION') or "videos"
    QUEUE_LOCATION = os.environ.get('QUEUE_LOCATION') or 'renderQueue'
    LOGS_LOCATION = os.environ.get('LOGS_LOCATION') or "logs" 
    RESOURCE_PATH = os.environ.get('RESOURCE_PATH') or 'resource'
    WATCHER_LOGS = os.environ.get('WATCHER_LOG') or 'renderWatcher'
    RENDER_LOGS = os.environ.get('RENDER_LOG') or 'renderService'
    FLASK_LOGS = os.environ.get('FLASK_LOG') or 'renderFlask'
    # Defining storage name and key
    STORAGE_ACCOUNT_NAME = os.environ.get('STORAGE_ACCOUNT_NAME') or 'csae48d5df47deax41bcxbaa'
    STORAGE_ACCOUNT_KEY = os.environ.get('STORAGE_ACCOUNT_KEY') or \
        'iUTL5cLSDTObfUliySlqjT4x1dfCQ1U7l7zuaZrPEwhGIHnHPKWfYuFrq16cCjFUS/122mcwJpdseC9JI6mSGA=='
    # TODO: When deploying, remove 'testingazure' for the commented out Share Name
    SHARE_NAME = os.environ.get('SHARE_NAME') or 'cs-william-squarev-media-10037ffe909d3982' 
    # Defining name of json file containing edits
    PROJECT_NAME = os.environ.get('PROJECT_NAME') or 'FinalSubclipJson.json'
    # TODO: The location of the resources (the silence mp3, default templates, etc.) may change
    # Defining location of generic 'resources' location
    RESOURCE_PATH = os.environ.get('RESOURCE_PATH') or 'resource'
    # Name of silence mp3
    SILENCE = os.environ.get('SILENCE') or 'silence.mp3'
    QUEUE_FOLDER = os.environ.get('QUEUE_FOLDER') or 'renderQueue'