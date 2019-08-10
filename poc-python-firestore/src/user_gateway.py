
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
        doc_ref = users_ref.document(client_id)
        preferences = doc_ref.collection("order").stream()

        doc = doc_ref.get()
        user_dict = UserGateway.convert_object_to_dict(doc)

        user_dict["order"] = UserGateway.convert_array_to_dict(preferences)


        return user_dict

    """
    def create(client):
        doc_ref = db.collection(collection_name).document()
        doc_ref.set(client)
        doc = doc_ref.get()

        doc_ref.collection(u"preferences").document().set(
            {
                u'type': u'language',
                u'name': u'java'
            }
        )

        doc_ref.collection(u"preferences").document().set(
            {
                u'type': u'language',
                u'name': u'python'
            }
        )

        response = {
            "message": "The client was created",
            "id": doc.id
        }

        return response
    """

    """
    def create(client):
        batch = db.batch()

        doc_ref = db.collection(collection_name).document()

        batch.set(doc_ref, client)

        doc = doc_ref.get()

        pref_01 = doc_ref.collection(u"preferences").document()
        batch.set(pref_01, {
            u'type': u'language',
            u'name': u'java'
        })

        raise Exception("JFF 02")

        pref_02 = doc_ref.collection(u"preferences").document()
        batch.set(pref_02, {
            u'type': u'language',
            u'name': u'python'        
        })

        batch.commit()

        response = {
            "message": "The client was created",
            "id": doc.id
        }

        return response
    """
    
    """
    def create(client):
        transaction = db.transaction()

        @firestore.transactional
        def update_in_transaction(transaction):
            doc_ref = db.collection(collection_name).document()

            transaction.set(doc_ref, client)

            doc = doc_ref.get()

            pref_01 = doc_ref.collection(u"preferences").document()
            transaction.set(pref_01, {
                u'type': u'language',
                u'name': u'java'
            })

            #raise Exception("JFF 02")

            pref_02 = doc_ref.collection(u"preferences").document()
            transaction.set(pref_02, {
                u'type': u'language',
                u'name': u'python'        
            })

            return doc.id

        id = update_in_transaction(transaction)

        response = {
            "message": "The client was created",
            "id": id
        }

        return response
    """


    def create(client):
        order_products = client["order"]
        del client["order"]

        client_ref = db.collection(collection_name).document()
        order_ref = client_ref.collection("order")
        
        
        client_ref.set(client)
        for product in order_products:
            order_ref.document().set(product)

        response = {
            "message": "The client was created",
            "id": client_ref.get().id
        }

        return response

    def update(client_id, client):
        users_ref = db.collection(collection_name).document(client_id)
        users_ref.set(client, merge=False)

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
        collection_ref = db.collection_group(u"order")
        #query = users_ref.where(u'age', u'>=', 18).where(u'age', u'<=', 30)
        #query = users_ref.where(u'last_name', u'==', "Augusto")
        #query = users_ref.where(u'preferences', u'array_contains', "typescript")
        query = collection_ref.where(u'product_id', u'==', 777)
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


    