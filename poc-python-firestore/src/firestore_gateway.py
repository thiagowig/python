from google.cloud import firestore

db = firestore.Client()

class FirestoreGateway():

    def __init__(self, collection_name):
        self.collection_name = collection_name


    