from flask import render_template
from flask_restplus import Api, Resource
from app import app

from app.sherpaEditor import driveClip

api = Api(app=app)


@api.route('/render/<string:proj_id>')
class RenderVideo(Resource):
    def get(self, proj_id):
        driveClip.render_video(
            uid=proj_id
        )


@api.route('/preview/<string:proj_id>')
class PreviewVideo(Resource):
    def get(self, proj_id):
        return driveClip.render_video(
                uid=proj_id,
                html_render=True
            )
