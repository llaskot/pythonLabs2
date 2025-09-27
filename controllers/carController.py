from models.carModel import CarModel


def get_all_cars():
    return CarModel.find_all()
