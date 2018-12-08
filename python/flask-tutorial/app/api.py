from app import app, db
from flask import request, Response
from flask_restplus import Api, Resource
import json

from app.models import Note

api = Api(app)


@api.route('/hello', methods=['GET'])
class HelloWorld(Resource):
    def get(self):
        return Response('hello world')


@api.route('/hello/json', methods=['GET'])
class HelloWorldJson(Resource):
    def get(self):
        return Response(json.dumps({
            'key': 'hello world'
        }), mimetype='application/json')


@api.route('/notes', methods=['GET', 'POST'])
class NoteCRUD(Resource):
    def get(self):
        notes = Note.query.all()
        return Response(json.dumps({
            'data': [note.as_dict() for note in notes],
        }), mimetype='application/json')

    def post(self):
        body = request.json
        db.session.add(Note(body['title'], body['content']))
        db.session.commit()
        return Response(json.dumps({
            'result': 'success'
        }), mimetype='application/json')
