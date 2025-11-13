from models.clientModel import ClientModel


def get_all_clients():
    return ClientModel.find_all()


def create_client(vals: tuple):
    client = ClientModel(
        vals[1] if vals[1] else None,
        vals[2] if vals[2] else None
    )
    if vals[0]:
        client.update_by_id(vals[0])
    else:
        client.create()


def get_client_by_id(car_id):
    return ClientModel.find_by("id", int(car_id))


def delete_client_by_id(client_id):
    return ClientModel.delete_by("id", int(client_id))


def search_client(val):
    return ClientModel.search(val)
