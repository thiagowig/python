from google.cloud import firestore
from flask import jsonify
from .client import Client

db = firestore.Client()

class FireStoreDao():    

    def list_all():
        users_ref = db.collection(u'users')
        docs = users_ref.stream()

        return jsonify({'clients': from_firestore(docs)})


    def list_one(client_id):
        users_ref = db.collection(u'users')
        doc = users_ref.document(client_id).get()
        client = Client.from_dict(doc.to_dict())

        return client.to_json()


    def create(client):
        doc_ref = db.collection(u'users').document()
        doc_ref.set(client)
        doc = doc_ref.get()

        client = Client.from_dict(doc.to_dict())

        return client.to_json()


    def update(client_id, client):
        users_ref = db.collection(u'users').document(client_id)
        users_ref.update(client)

        return jsonify({'message': 'The client was updated'})


    def delete(client_id):
        users_ref = db.collection(u'users')
        users_ref.document(client_id).delete()

        return jsonify({'message': 'The client was deleted'})


def from_firestore(docs):
    my_dict = { doc.id: doc.to_dict() for doc in docs }
    return my_dict
