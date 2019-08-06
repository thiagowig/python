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
    client = request.json
    return DataBase.create(client)


@crud.route('/clients/<client_id>', methods=['PUT'])
def update(client_id):
    client = request.json
    return DataBase.update(client_id, client)


@crud.route('/clients/<client_id>', methods=['DELETE'])
def delete(client_id):
    return DataBase.delete(client_id)


@crud.route('/clients/retired', methods=['GET'])
def retired():
    retired_age = 65
    return DataBase.find_by_age_greater_than(retired_age)