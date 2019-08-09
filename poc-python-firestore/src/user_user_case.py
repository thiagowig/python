from src.user_gateway import UserGateway as gateway

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


    def find_by_age_greater_than(age):
        return gateway.find_by_age_greater_than(age)
