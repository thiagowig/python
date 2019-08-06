from flask import Blueprint, jsonify, abort, make_response, request
from src.database import DataBase

crud = Blueprint('crud', __name__)

@crud.route('/clients', methods=['GET'])
def list():
    return DataBase.list_all()


@crud.route('/clients/<client_id>', methods=['GET'])
def list_one(client_id):
    return DataBase.list_one(client_id)


@crud.route('/clients', methods=['POST'])
def create():
    print('Create')


@crud.route('/clients/<client_id>', methods=['PUT'])
def update(client_id):
    print('Update')


@crud.route('/clients/<client_id>', methods=['DELETE'])
def delete(client_id):
    print('Delete')


def create_client(document, first_name, last_name):
    doc_ref = db.collection(u'users').document(document)
    doc_ref.set({
        u'first': first_name,
        u'last': last_name
    })
    
