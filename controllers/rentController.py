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
        return {f"{row[2]} :: {row[1]}": row[0] for row in res["values"]}
    except Exception as e:
        raise e


def get_cars_list(val):
    try:
        res = CarModel.search_available_cars('license_plates', val)
        return {f"{row[4]} :: {row[1]}": row[0] for row in res["values"]}
    except Exception as e:
        raise e


def prepare_data(car_id: int, client_id: int, date, days_qty):
    try:
        if not car_id or not client_id or not date or not days_qty:
            raise ValueError("All the fields are required!!!")
        car = get_car(car_id)
        client = ClientModel.find_by("id", client_id)
        return {
            'client_id': client["values"][0][0],
            'client_name': client["values"][0][1],
            'client_license': client["values"][0][2],
            'car_id': car["values"][0][0],
            'car_model': car["values"][0][1],
            'license_plates': car["values"][0][4],
            'start_day': date.strftime("%Y-%m-%d"),
            'days_number': days_qty,
            'rent_per_day': car["values"][0][5],
            'rent_total': car["values"][0][5] * int(days_qty),
            'insurance_per_day': car["values"][0][6],
            'insurance_total': car["values"][0][6] * int(days_qty),
            'total_price': car["values"][0][5] * int(days_qty) + car["values"][0][6] * int(days_qty)
        }
    except Exception as e:
        raise e


def save_rent(car_id, client_id, days_qty, total_price, start_date):
    try:
        rent = RentModel(car_id, client_id, days_qty, total_price, start_date)
        car = CarModel(None, None, None, None, None, None, 0)
        car.update_by_id(car_id)
        rent.create()
        return True
    except Exception as e:
        raise e


def change_statuses(rent_id):
    try:
        car = CarModel(None, None, None, None, None, None, 1)
        rent = RentModel(None, None, None, None, None, 0)
        old_rent = RentModel.find_by("id", rent_id)
        if old_rent["values"][0][6] == 0:
            return False
        car_id = old_rent["values"][0][1]
        car.update_by_id(car_id)
        rent.update_by_id(rent_id)
        return True
    except Exception as e:
        raise e


if __name__ == "__main__":
    print(get_cars_list(''))
