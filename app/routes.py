from flask import render_template
from flask_restplus import Api, Resource
from app import app
from multiprocessing import Process
from app.queueMaker import queue_service
api = Api(app=app)


@api.route('/render/<string:proj_id>')
class RenderVideo(Resource):
    def get(self, proj_id):
        p = Process(target=queue_service.create_queue, args=(proj_id,))
        p.start()
        p.join()
        print("Process complete")
        #p.close()


@api.route('/sherpatemplatestatus/<string:projectid>')
class RenderVideoStatus(Resource):
    def get(self, proj_id):
        p = Process(target=queue_service.get_queue_status, args=(proj_id,))
        p.start()
        p.join()
        print("Process complete")