from models.carModel import CarModel


def get_all_cars():
    try:
        return CarModel.find_all()
    except Exception as e:
        raise e


def create_car(vals: tuple):
    try:
        car = CarModel(
            vals[1] if vals[1] else None,
            int(vals[2]) if vals[2] else None,
            vals[3] if vals[3] else None,
            vals[4] if vals[4] else None,
            float(vals[5]) if vals[5] else None,
            float(vals[6]) if vals[6] else None,
            bool(vals[7]) if vals[7] else False
        )
        if vals[0]:
            car.update_by_id(vals[0])
        else:
            car.create()
    except Exception as e:
        raise e


def get_car_by_id(car_id):
    try:
        return CarModel.find_by("id", car_id)
    except Exception as e:
        raise e
