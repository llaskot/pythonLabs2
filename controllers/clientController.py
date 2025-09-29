from models.clientModel import ClientModel


def get_all_clients():
    try:
        return ClientModel.find_all()
    except Exception as e:
        raise e
