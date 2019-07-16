from notes import get_model
from flask import Blueprint, jsonify, abort, make_response, request

crud = Blueprint('crud', __name__)

noteTypes = [
    {
        'id': 1,
        'name': 'Cloud'
    },
    {
        'id': 2,
        'name': 'Frontend'
    },
    {
        'id': 3,
        'name': 'Backend'
    }
]

@crud.route('/v1.0/noteTypes')
def list():
    noteTypesList = get_model().list()

    return jsonify({'noteTypes': noteTypesList})


@crud.route('/v1.0/noteTypes/<int:noteType_id>', methods=['GET'])
def get_noteType(noteType_id):
    noteType = get_model().read(noteType_id)    
    
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
    noteType = get_note_type(noteType_id)

    if not request.json or not 'name' in request.json:
        abort(400)

    noteType[0]['name'] = request.json.get('name', noteType[0]['name'])

    return jsonify({'noteType': noteType[0]})


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


