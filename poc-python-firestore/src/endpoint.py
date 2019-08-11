from flask import Blueprint, request, Response
from src.user_user_case import UserUseCase as use_case
import json

endpoint = Blueprint('endpoint', __name__)

@endpoint.route('/users')
def list():
    response_data = use_case.list_all()

    return create_response(response_data)


@endpoint.route('/users/<user_id>')
def list_one(user_id):
    response_data = use_case.list_one(user_id)

    return create_response(response_data)


@endpoint.route('/users', methods=['POST'])
def create():
    request_data = request.json
    response_data = use_case.create(request_data)

    return create_response(response_data, 201)


@endpoint.route('/users/<user_id>', methods=['PUT'])
def update(user_id):
    request_data = request.json
    response_data = use_case.update(user_id, request_data)

    return create_response(response_data)


@endpoint.route('/users/<user_id>', methods=['DELETE'])
def delete(user_id):
    response_data = use_case.delete(user_id)

    return create_response(response_data)


@endpoint.route('/users/lab')
def lab():
    response_data = use_case.lab()

    return create_response(response_data)


@endpoint.route('/clear')
def clear():
    response_data = use_case.clear()

    return create_response(response_data)


def create_response(data, status = 200):
    data  = json.dumps(data)
    return Response(response=data, status=status, mimetype="application/json")
    