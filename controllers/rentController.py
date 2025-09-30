from models.clientModel import ClientModel
from models.rentModel import RentModel
from models.carModel import CarModel



def get_all_rents():
    try:
        return RentModel.get_full_info()
    except Exception as e:
        raise e

def get_car(car_id):
    try:
        return CarModel.find_by('id', car_id)
    except Exception as e:
        raise e


def search_rent(val):
    try:
        return RentModel.search(val)
    except Exception as e:
        raise e


def get_users_list(val):
    try:
        res = ClientModel.search_single_str('license_num', val)
        return {f"{row[2]}: {row[1]}": row[0] for row in res["values"]}
    except Exception as e:
        raise e


def get_cars_list(val):
    try:
        res = CarModel.search_single_str('license_plates', val)
        return {f"{row[4]}: {row[1]}": row[0] for row in res["values"]}
    except Exception as e:
        raise e

if __name__ == "__main__":
    print(get_cars_list(''))
