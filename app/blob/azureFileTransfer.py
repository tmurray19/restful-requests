from app import app
import json
from azure.storage.file import FileService


def create_share_dir(proj_id):
    """Creates a directory at the share location"""
    file_service = FileService(
        account_name=app.config['STORAGE_ACCOUNT_NAME'],
        account_key=app.config['STORAGE_ACCOUNT_KEY'],
    )

    file_service.create_share(app.config['SHARE_NAME'])

    file_service.create_directory(app.config['SHARE_NAME'], proj_id)

    return file_service


def upload_file(proj_id, name, local_path, file_service):
    """Uploads a generic file to the File Share, given name, local path, & project id"""
    file_service.create_file_from_path(
        app.config['SHARE_NAME'],
        proj_id,
        name,
        local_path
    )


def get_json(proj_id, file_service):
    """Looks for directory in azure storage with the project id specified, and returns the json data
    (JSON data is returned as string first, then converted to json with corresponding python library)"""

    azure_file = file_service.get_file_to_text(
        app.config['SHARE_NAME'],
        proj_id,
        app.config['PROJECT_NAME']
    ).content

    json_data = json.loads(azure_file)

    return json_data
