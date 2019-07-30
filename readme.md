# Flask app
## This version tries to implement the config file, so that all the common calls are defined in one succint location
Flask app implementing Video Sherpa Editor

## Walk through:
    - User is authenticated elsewhere, with project id
    - Project ID is passed into this docker image
    - Python file looks for directory in Azure with Project ID
    - Opens File System, and opens JSON file containing edit data
    - Directory is mounted to image
    - File Driver looks through JSON data
    - Python file looks for all files in mounted directory
    - Edits are made on video file as it shows up in JSON
    - Audio is concatenated together
    - Full quality video is written to docker image
    - or it's written to mounted directory
     