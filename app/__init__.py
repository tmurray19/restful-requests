from flask import Flask
from config import Config

# Initialising Code
app = Flask(__name__)
# Config file
app.config.from_object(Config)

from app import routes