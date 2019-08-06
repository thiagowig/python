from google.cloud import firestore
from flask import jsonify

db = firestore.Client()

class FireStoreDao():    

    def list_all():
        users_ref = db.collection(u'users')
        docs = users_ref.stream()

        return jsonify({'clients': from_firestore(docs)})


    def list_one(client_id):
        users_ref = db.collection(u'users')
        docs = users_ref.where(u'first', u'==', u'thiago').stream()

        print(docs)

        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))
        
        return jsonify({'clients': from_firestore(docs)})


def from_firestore(docs):
    my_dict = { doc.id: doc.to_dict() for doc in docs }
    return my_dict
