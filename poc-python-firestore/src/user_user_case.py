from src.firestore_gateway import FirestoreGateway

collection_name = "users"
gateway = FirestoreGateway(collection_name)

class UserUseCase():

    def list_all():
        return gateway.list_all()


    def list_one(user_id):
        return gateway.list_one(user_id)


    def create(user):
        return gateway.create(user)


    def update(user_id, user):
        return gateway.update(user_id, user)


    def delete(user_id):
        return gateway.delete(user_id)


    def lab():
        return gateway.lab()


    def clear():
        return gateway.clear()


    
