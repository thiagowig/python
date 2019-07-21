from notes import get_model
from flask import Blueprint, jsonify, abort, make_response, request, current_app

import logging
import requests
from logging.handlers import RotatingFileHandler

crud = Blueprint('crud', __name__)

@crud.route('/v1.0/noteTypes')
def list():
    noteTypesList = get_model().list()

    return jsonify({'noteTypes': noteTypesList})


@crud.route('/v1.0/noteTypes/<int:noteType_id>', methods=['GET'])
def get_noteType(noteType_id):
    noteType = get_model().read(noteType_id)

    url = current_app.config['FUNCTION_URL']
    payload = {"message": "noteType.name"}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=payload, headers=headers)
    current_app.logger.info('SERÁ QUE FOI. STATUS: %s', r.status_code)
    current_app.logger.info('SERÁ QUE FOI. TEXT: %s', r.text)
    
    return jsonify({'noteType': noteType})


@crud.route('/v1.0/noteTypes', methods=['POST'])
def create_noteType():
    if not request.json or not 'name' in request.json:
        abort(400)

    data = request.json    
    noteType = get_model().create(data)

    return jsonify({'noteType': noteType}), 201


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

@crud.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def get_note_type(noteType_id):
    noteType = [noteType for noteType in noteTypes if noteType['id'] == noteType_id]
    if len(noteType) == 0:
        abort(404)

    return noteType


