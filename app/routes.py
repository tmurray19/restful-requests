from flask import render_template
from flask_restplus import Api, Resource
from app import app
from multiprocessing import Process
from app.queueMaker import queue_service
from datetime import datetime
import os
import logging


"""now = datetime.now()
log_name = os.path.join(app.config['LOGS_LOCATION'], app.config['FLASK_LOGS'], now.strftime("%Y-%m-%d-%H:%M:%S")+"_render_flask_instance.txt")
log_name = 'G:\\mnt\\csae48d5df47deax41bcxbaa\\logs\\render_flask\\2019-08-08-18.01.22_render_flask_instance.txt'
logging.basicConfig(
    level=logging.DEBUG,
    filemode="w+",
    filename=log_name
)
logging.info("Flask instances started")
"""
api = Api(app=app)


@api.route('/render/<string:proj_id>')
class RenderVideo(Resource):
    def get(self, proj_id):
        queue_create = queue_service.create_queue(proj_id)
        return queue_create


@api.route('/sherpatemplatestatus/<string:proj_id>')
class RenderVideoStatus(Resource):
    def get(self, proj_id):
        queue_status = queue_service.get_queue_status(proj_id)
        return queue_status
