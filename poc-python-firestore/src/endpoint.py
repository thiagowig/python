from flask import Blueprint, request, Response
from src.user_user_case import UserUseCase as use_case
import json

endpoint = Blueprint('endpoint', __name__)

@endpoint.route('/clients')
def list():
    response_data = use_case.list_all()

    return create_response(response_data)


@endpoint.route('/clients/<client_id>')
def list_one(client_id):
    response_data = use_case.list_one(client_id)

    return create_response(response_data)


@endpoint.route('/clients', methods=['POST'])
def create():
    request_data = request.json
    response_data = use_case.create(request_data)

    return create_response(response_data, 201)


@endpoint.route('/clients/<client_id>', methods=['PUT'])
def update(client_id):
    request_data = request.json
    response_data = use_case.update(client_id, request_data)

    return create_response(response_data)


@endpoint.route('/clients/<client_id>', methods=['DELETE'])
def delete(client_id):
    response_data = use_case.delete(client_id)

    return create_response(response_data)


@endpoint.route('/clients/retired')
def retired():
    retired_age = 65
    response_data = use_case.find_by_age_greater_than(retired_age)

    return create_response(response_data)


@endpoint.route('/clear')
def clear():
    response_data = use_case.clear()

    return create_response(response_data)


def create_response(data, status = 200):
    data  = json.dumps(data)
    return Response(response=data, status=status, mimetype="application/json")
    