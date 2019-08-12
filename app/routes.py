from flask import render_template
from flask_restplus import Api, Resource
from app import app
from multiprocessing import Process
from app.queueMaker import queue_service
api = Api(app=app)


@api.route('/render/<string:proj_id>&compressed_render=<int:compressed_render>')
class RenderVideo(Resource):
    def get(self, proj_id, compressed_render):
        p = Process(target=queue_service.create_queue, args=(proj_id,compressed_render,))
        p.start()
        p.join()
        print("Process complete")
        #p.close()