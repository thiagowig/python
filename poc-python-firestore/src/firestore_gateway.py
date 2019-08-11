from google.cloud import firestore

db = firestore.Client()

class FirestoreGateway():

    def __init__(self, collection_name):
        self.collection_name = collection_name


    def list_all(self):
        collection_ref = db.collection(self.collection_name)
        docs = collection_ref.stream()

        response = self.generate_array_response(docs)

        return response


    def create(self, user):
        collection_ref = db.collection(self.collection_name)
        doc_ref = collection_ref.document()
        doc_ref.set(user)

        doc = doc_ref.get()

        return {"id": doc.id}

    
    def list_one(self, client_id):
        doc_ref = self.get_doc_ref(self.collection_name, client_id)
        doc = doc_ref.get()

        fields = doc.to_dict()
        fields["id"] = doc.id

        return fields


    def update(self, client_id, client):
        doc_ref = self.get_doc_ref(self.collection_name, client_id)
        doc_ref.set(client, merge=True)

        return {"message": "Success"}


    def delete(self, client_id):
        doc_ref = self.get_doc_ref(self.collection_name, client_id)
        doc_ref.delete()

        return {"message": "Success"}


    def query(self):
        collection_ref = db.collection(self.collection_name)
        query = collection_ref.where("last_name", "==", "Ferreira")
        query = query.where("age", ">=", 30)
        docs = query.stream()

        response = self.generate_array_response(docs)

        return response

    def generate_array_response(self, docs):
        array = []

        for doc in docs:
            fields = doc.to_dict()
            fields["id"] = doc.id

            array.append(fields)

        return array


    def get_doc_ref(self, collection_name, document_id):
        collection_ref = db.collection(self.collection_name)
        doc_ref = collection_ref.document(document_id)

        return doc_ref
        