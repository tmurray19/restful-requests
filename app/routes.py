from flask import render_template
from flask_restplus import Api, Resource
from app import app
from multiprocessing import Process
from app.sherpaEditor import driveClip

api = Api(app=app)


@api.route('/render/<string:proj_id>')
class RenderVideo(Resource):
    def get(self, proj_id):
        p = Process(target=driveClip.render_video, args=(proj_id,))
        p.start()
        p.join()
        #p.close()



@api.route('/preview/<string:proj_id>')
class PreviewVideo(Resource):
    def get(self, proj_id):
        p = Process(target=driveClip.render_video, args=(proj_id, True,))
        p.start()
        p.join()
        #p.close()
