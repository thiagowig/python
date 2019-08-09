

from google.cloud import firestore
from .client import Client
from dataclasses import dataclass

db = firestore.Client()

class UserGateway():          

    def list_all():
        users_ref = db.collection(u'users')
        docs = users_ref.stream()

        return UserGateway.convert_array_to_dict(docs)


    def list_one(client_id):
        users_ref = db.collection(u'users')
        doc = users_ref.document(client_id).get()

        return UserGateway.convert_object_to_dict(doc)


    def create(client):
        doc_ref = db.collection(u'users').document()
        doc_ref.set(client)
        doc = doc_ref.get()

        response = {
            "message": "The client was created",
            "id": doc.id
        }

        return response


    def update(client_id, client):
        users_ref = db.collection(u'users').document(client_id)
        users_ref.update(client)

        return {'message': 'The client was updated'}


    def delete(client_id):
        users_ref = db.collection(u'users')
        users_ref.document(client_id).delete()

        return {'message': 'The client was deleted'}


    def find_by_age_greater_than(age):
        users_ref = db.collection(u'users')
        query = users_ref.where(u'age', u'>=', 50).where(u'age', u'<=', 67)
        docs = query.stream()

        return {'clients': UserGateway.convert_array_to_dict(docs)}


    def convert_array_to_dict(docs):
        array = []

        for doc in docs:
            array.append(UserGateway.convert_object_to_dict(doc))

        return array


    def convert_object_to_dict(doc):
        fields = doc.to_dict()
        fields["id"] = doc.id

        return fields


    