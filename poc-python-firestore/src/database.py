from src.firestore_dao import FireStoreDao as store

class DataBase():

    def list_all():
        return store.list_all()


    def list_one(client_id):
        return store.list_one(client_id)


    def create(client):
        return store.create(client)


    def update(client_id, client):
        return store.update(client_id, client)


    def delete(client_id):
        return store.delete(client_id)


    def find_by_age_greater_than(age):
        return store.find_by_age_greater_than(age)