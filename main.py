from flask import Flask
from flask_restful import Api, Resource,reqparse,abort

app = Flask(__name__)
api = Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:8452691@localhost/entreprise'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entreprise-sqlite.db'

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type = str, help ="Name of the video is required", required =True)
video_put_args.add_argument("views", type = str, help ="views of the video is required", required =True)
video_put_args.add_argument("likes", type = str, help ="Likes of the video is required", required =True)

videos ={}



class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    def put(self, video_id):
        args  = video_put_args.parse_args()
        return {video_id : args}

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug = True)