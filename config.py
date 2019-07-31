import os

"""
import secrets


secrets.token_urlsafe(32)
"""

basedir = os.path.abspath(os.path.dirname(__file__))


# Config file
class Config(object):
    # Secret key used for verification
    # or statements are used as a fallback
    SECRET_KEY = os.environ.get('SECRET_KEY') or "WgnYVzwgwF7Alu1B3DehuO-C-QoKcBitsHqpiFi1cRE"
    # Attach directory as well (Though neither of these are necessary)
    DIR_LOCATION = os.environ.get('DIR_LOCATION') or "D:/project"
    # Defining storage name and key
    STORAGE_ACCOUNT_NAME = os.environ.get('STORAGE_ACCOUNT_NAME') or 'csae48d5df47deax41bcxbaa'
    STORAGE_ACCOUNT_KEY = os.environ.get('STORAGE_ACCOUNT_KEY') or \
        'iUTL5cLSDTObfUliySlqjT4x1dfCQ1U7l7zuaZrPEwhGIHnHPKWfYuFrq16cCjFUS/122mcwJpdseC9JI6mSGA=='
    # Defining name of share in azure files
    SHARE_NAME = os.environ.get('SHARE_NAME') or 'testingazure'  # 'cs-william-squarev-media-10037ffe909d3982'
    # Defining name of json file containing edits
    PROJECT_NAME = os.environ.get('PROJECT_NAME') or 'FinalSubclipJson.json'
    # Defining location of generic 'resources' location
    RESOURCE_PATH = os.environ.get('RESOURCE_PATH') or 'resource'
    # Name of silence mp3
    SILENCE = os.environ.get('SILENCE') or 'silence.mp3'
