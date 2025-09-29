from models.clientModel import ClientModel


def get_all_clients():
    try:
        return ClientModel.find_all()
    except Exception as e:
        raise e


def create_client(vals: tuple):
    try:
        client = ClientModel(
            vals[1] if vals[1] else None,
            vals[2] if vals[2] else None
        )
        if vals[0]:
            client.update_by_id(vals[0])
        else:
            client.create()
    except Exception as e:
        raise e


def get_client_by_id(car_id):
    try:
        return ClientModel.find_by("id", int(car_id))
    except Exception as e:
        raise e


def delete_client_by_id(client_id):
    try:
        return ClientModel.delete_by("id", int(client_id))
    except Exception as e:
        raise e


def search_client(val):
    try:
        return ClientModel.search(val)
    except Exception as e:
        raise e
