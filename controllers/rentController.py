from models.clientModel import ClientModel
from models.rentModel import RentModel
from models.carModel import CarModel


def get_all_rents():
    return RentModel.get_full_info()


def get_car(car_id):
    return CarModel.find_by('id', car_id)


def search_rent(val):
    return RentModel.search_full_info(val)


def get_users_list(val):
    res = ClientModel.search_single_str('license_num', val)
    return {f"{row[2]} :: {row[1]}": row[0] for row in res["values"]}


def get_cars_list(val):
    res = CarModel.search_available_cars('license_plates', val)
    return {f"{row[4]} :: {row[1]}": row[0] for row in res["values"]}


def prepare_data(car_id: int, client_id: int, date, days_qty):
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


def save_rent(car_id, client_id, days_qty, total_price, start_date):
    rent = RentModel(car_id, client_id, days_qty, total_price, start_date)
    car = CarModel(None, None, None, None, None, None, 0)
    car.update_by_id(car_id)
    rent.create()
    # return True


def change_statuses(rent_id):
    car = CarModel(None, None, None, None, None, None, 1)
    rent = RentModel(None, None, None, None, None, 0)
    old_rent = RentModel.find_by("id", rent_id)
    if old_rent["values"][0][6] == 0:
        return False
    car_id = old_rent["values"][0][1]
    car.update_by_id(car_id)
    rent.update_by_id(rent_id)
    return True


# if __name__ == "__main__":
#     print(get_cars_list(''))
