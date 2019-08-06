from src.firestore_dao import FireStoreDao

class DataBase():
    def list_all():
        return FireStoreDao.list_all()

    def list_one(client_id):
        return FireStoreDao.list_one(client_id)