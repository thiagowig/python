
from google.cloud import firestore

db = firestore.Client()
collection_name = u'users'

class UserGateway():          

    def list_all():
        users_ref = db.collection(collection_name)
        docs = users_ref.stream()

        return UserGateway.convert_array_to_dict(docs)


    def list_one(client_id):
        users_ref = db.collection(collection_name)
        doc = users_ref.document(client_id).get()

        return UserGateway.convert_object_to_dict(doc)


    def create(client):
        doc_ref = db.collection(collection_name).document()
        doc_ref.set(client)
        doc = doc_ref.get()

        doc_ref.collection("preferences").document().set(
            {
                u'type': u'language',
                u'name': u'java'
            }
        )


        response = {
            "message": "The client was created",
            "id": doc.id
        }

        return response


    def update(client_id, client):
        users_ref = db.collection(collection_name).document(client_id)
        users_ref.update(client)

        return {'message': 'The client was updated'}


    def delete(client_id):
        users_ref = db.collection(collection_name)
        users_ref.document(client_id).delete()

        return {'message': 'The client was deleted'}


    def clear():
        docs = UserGateway.list_all()
        for doc in docs:
            id = doc["id"]
            UserGateway.delete(id)

        return {'message': f'The collection {collection_name} was cleared'}


    def find_by_age_greater_than(age):
        users_ref = db.collection(collection_name)
        #query = users_ref.where(u'age', u'>=', 18).where(u'age', u'<=', 30)
        #query = users_ref.where(u'last_name', u'==', "Augusto")
        #query = users_ref.where(u'preferences', u'array_contains', "typescript")
        docs = query.stream()

        return UserGateway.convert_array_to_dict(docs)


    def convert_array_to_dict(docs):
        array = []

        for doc in docs:
            array.append(UserGateway.convert_object_to_dict(doc))

        return array


    def convert_object_to_dict(doc):
        fields = doc.to_dict()

        if fields is None:
            return {}

        else:
            fields["id"] = doc.id
            return fields


    