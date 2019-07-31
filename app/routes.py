from flask import render_template, make_response
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
        headers = {'Content-type': 'text/html'}
        return make_response(
            render_template(
                'proj_render.html',
                title="In browser preview",
                project_preview=driveClip.render_video(
                    uid=proj_id,
                    html_render=True
                )
                ),
            200,
            headers
        )
