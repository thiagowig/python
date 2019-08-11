from src.firestore_gateway import FirestoreGateway

collection_name = "users"
gateway = FirestoreGateway(collection_name)

class UserUseCase():

    def list_all():
        return gateway.list_all()


    def list_one(client_id):
        return gateway.list_one(client_id)


    def create(client):
        return gateway.create(client)


    def update(client_id, client):
        return gateway.update(client_id, client)


    def delete(client_id):
        return gateway.delete(client_id)


    def clear():
        return gateway.clear()


    def query():
        return gateway.query()
