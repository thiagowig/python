from notes import get_model
from flask import Blueprint, jsonify, abort, make_response, request, current_app

import logging
import requests
import base64
from logging.handlers import RotatingFileHandler
from google.cloud import pubsub_v1

crud = Blueprint('crud', __name__)

MESSAGES = []

@crud.route('/v1.0/noteTypes')
def list():
    noteTypesList = get_model().list()

    return jsonify({'noteTypes': noteTypesList})


@crud.route('/v1.0/noteTypes/<int:noteType_id>', methods=['GET'])
def get_noteType(noteType_id):
    noteType = get_model().read(noteType_id)

    """
    url = current_app.config['FUNCTION_URL']
    payload = {"message": "noteType.name"}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=payload, headers=headers)
    """
    
    return jsonify({'noteType': noteType})


@crud.route('/v1.0/noteTypes', methods=['POST'])
def create_noteType():
    if not request.json or not 'name' in request.json:
        abort(400)

    data = request.json    
    noteType = get_model().create(data)

    json_response = jsonify({'noteType': noteType})

    send_message(json_response)

    return json_response, 201

def send_message(noteType):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(
        current_app.config['PROJECT'],
        current_app.config['PUBSUB_TOPIC'])

    publisher.publish(topic_path, data="noteType".encode('utf-8'))



@crud.route('/v1.0/noteTypes/<int:noteType_id>', methods=['PUT'])
def update_noteType(noteType_id):
    if not request.json or not 'name' in request.json:
        abort(400)

    noteType = get_model().read(noteType_id)
    data = request.json

    noteType = get_model().update(data, noteType_id)

    return jsonify({'noteType': noteType})


@crud.route('/v1.0/noteTypes/<int:noteType_id>', methods=['DELETE'])
def detele_noteType(noteType_id):
    get_model().delete(noteType_id)

    return jsonify({'result': True})


@crud.route('/pubsub/push', methods=['POST'])
def pubsub_push():
    if (request.args.get('token') != current_app.config['PUBSUB_VERIFICATION_TOKEN']):
        return 'Invalid request', 400

    envelope = json.loads(request.data.decode('utf-8'))
    payload = base64.b64decode(envelope['message']['data'])

    MESSAGES.append(payload)

    return 'OK', 200

@crud.route('/pubsub', methods=['GET'])
def pubsub_list():
    return jsonify(MESSAGES)



@crud.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def get_note_type(noteType_id):
    noteType = [noteType for noteType in noteTypes if noteType['id'] == noteType_id]
    if len(noteType) == 0:
        abort(404)

    return noteType


