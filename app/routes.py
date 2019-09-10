from flask import render_template
from flask_restplus import Api, Resource
from app import app
from multiprocessing import Process
from app.queueMaker import queue_service
from datetime import datetime
import os
import logging

api = Api(app=app)


@api.route('/render/<string:proj_id>&compressed_render=<int:compressed_render>')
@api.route('/render/<string:proj_id>')
@api.route('/render/<string:proj_id>&chunk_render=<int:chunk_render>')
class RenderVideo(Resource):
    def get(self, proj_id, compressed_render=0, chunk_render=0):
        logging.debug("Creating render request for project '{}' with compress render of '{}' & chunk render of '{}'".format(proj_id, compressed_render, chunk_render))
        queue_create = queue_service.create_queue(proj_id, compressed_render, chunk_render)
        return queue_create


@api.route('/renderstatus/<string:proj_id>&compressed_render=<int:compressed_render>')
@api.route('/renderstatus/<string:proj_id>')
@api.route('/renderstatus/<string:proj_id>&chunk_render=<int:chunk_render>')
class RenderVideoStatus(Resource):
    def get(self, proj_id, compressed_render=0, chunk_render=0):
        logging.debug("Querying for render status of '{}'".format(proj_id))
        queue_status = queue_service.get_queue_status(proj_id, compressed_render, chunk_render)
        return queue_status
