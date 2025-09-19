from models.carModel import CarModel
from models.clientModel import ClientModel
from models.rentModel import RentModel

if __name__ == '__main__':
    # car = CarModel("Honda Civ", 2019, "Blue", "XYZ789", 45, 12)
    # newCar = car.create()
    # print(newCar)

    # car = CarModel("AAA", None, "Blueaa", None)
    # newCar = car.update_by_id(1)
    # print(newCar)

    # print(CarModel.find_by('id', 1))
    # print(CarModel.find_by('day_price', '45'))

    # print(CarModel.delete_by('id', 3))



    # clint = ClientModel("Pupkin WS", "AZ111222")
    # res = clint.create()
    # print(res)

    # print(ClientModel.delete_by('id', 6))

    rent = RentModel(3, 5, 4, 800)
    res = rent.create()
    print(res)