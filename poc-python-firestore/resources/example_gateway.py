from google.cloud import firestore

db = firestore.Client()

class FirestoreGateway():

    def __init__(self, collection_name):
        self.collection_name = collection_name
        self._max_attempts = 2


    def list_all(self):
        collection_ref = db.collection(self.collection_name)
        docs = collection_ref.stream()

        response = self.generate_array_response(docs)

        return response


    def create(self, user):
        doc_ref = self.get_doc_ref(collection_name=self.collection_name)
        
        workouts = user.get("workouts")
        del user["workouts"]
        
        doc_ref.set(user)
        
        self.save_workouts(doc_ref, workouts)

        return {"id": doc_ref.get().id}

    def save_workouts(self, doc_ref, workouts):
        workout_ref = doc_ref.collection("workouts")

        for workout in workouts:
            work_doc_ref = workout_ref.document(workout["id"])
            work_doc_ref.set(workout)

    
    def list_one(self, user_id):
        doc_ref = self.get_doc_ref(self.collection_name, user_id)
        doc = doc_ref.get()

        fields = doc.to_dict()
        fields["id"] = doc.id
        
        workouts = doc_ref.collection("workouts").stream()
        fields["workouts"] = self.generate_array_response(workouts)

        return fields


    def update(self, user_id, user):
        doc_ref = self.get_doc_ref(self.collection_name, user_id)
        doc_ref.set(user, merge=True)

        return {"message": "Success"}


    def delete(self, user_id):
        doc_ref = self.get_doc_ref(self.collection_name, user_id)
        doc_ref.delete()

        return {"message": "Success"}


    """
    def lab(self):
        batch = db.batch()

        doc_01 = self.get_doc_ref(self.collection_name)
        batch.set(doc_01, {
            "first_name": "Cesar",
            "last_name": "Gon"
        })

        raise Exception("Just for fun")

        doc_02 = self.get_doc_ref(self.collection_name)
        batch.set(doc_02, {
            "first_name": "Lyoto",
            "last_name": "Machida"
        })

        batch.commit()

    
    def lab(self):
        collection_ref = db.collection(self.collection_name)
        query = collection_ref.where("last_name", "==", "Ferreira")
        query = query.where("age", ">=", 30)
        docs = query.stream()

        response = self.generate_array_response(docs)

        return response
    """
    
    def lab(self):
        transaction = db.transaction()

        @firestore.transactional
        def update_in_transaction(self, transaction):
            doc_ref = self.get_doc_ref("1Q6qbVmjTY3JPBC3z1Sr")
            doc = doc_ref.get(transaction=transaction)

            transaction.update(doc_ref, {
                u"first_name", doc.get("first_name") + doc.get("last_name") 
            })

        update_in_transaction(self, transaction)

        return {"message": "Success"}
    

    def generate_array_response(self, docs):
        array = []

        for doc in docs:
            fields = doc.to_dict()
            fields["id"] = doc.id

            array.append(fields)

        return array


    def get_doc_ref(self, collection_name, document_id=None):
        collection_ref = db.collection(self.collection_name)

        if document_id:
            doc_ref = collection_ref.document(document_id)
        else:
            doc_ref = collection_ref.document()

        return doc_ref

    
    def _clean_up(self):
        pass
        