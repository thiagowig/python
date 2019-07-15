from flask import Flask, jsonify, abort, make_response, request
app = Flask(__name__)

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

@app.route('/api/v1.0/noteTypes')
def get_noteTypes():
    return jsonify({'noteTypes': noteTypes})


@app.route('/api/v1.0/noteTypes/<int:noteType_id>', methods=['GET'])
def get_noteType(noteType_id):
    noteType = get_note_type(noteType_id)    
    
    return jsonify({'noteType': noteType[0]})


@app.route('/api/v1.0/noteTypes', methods=['POST'])
def create_noteType():
    if not request.json or not 'name' in request.json:
        abort(400)


    noteType = {
        'id': noteTypes[-1]['id'] + 1,
        'name': request.json['name']
    }

    noteTypes.append(noteType)

    return jsonify({'noteType': noteType}), 201


@app.route('/api/v1.0/noteTypes/<int:noteType_id>', methods=['PUT'])
def update_noteType(noteType_id):
    noteType = get_note_type(noteType_id)

    if not request.json or not 'name' in request.json:
        abort(400)

    noteType[0]['name'] = request.json.get('name', noteType[0]['name'])

    return jsonify({'noteType': noteType[0]})


@app.route('/api/v1.0/noteTypes/<int:noteType_id>', methods=['DELETE'])
def detele_noteType(noteType_id):
    noteType = get_note_type(noteType_id)
    noteTypes.remove(noteType[0])

    return jsonify({'result': True})


def get_note_type(noteType_id):
    noteType = [noteType for noteType in noteTypes if noteType['id'] == noteType_id]
    if len(noteType) == 0:
        abort(404)

    return noteType


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)