# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None


is_b = bool(input("введите True если в машие будет ехать ребенок, Flse если ребенка не будет: "))
count_p = int(input("введите количество пассажиров с учетом ребенка (если он есть): "))


class Taxi:

    def __init__(self, count_passenger: int, car_numb: int, is_baby: bool, is_busy: bool):
        self.cp = count_passenger
        self.baby = is_baby
        self.busy = is_busy
        self.c_numb = car_numb
        # self.cars = cars

    def find_car(self, count_passengers, is_baby):
            for car in self.cars:
                if not car.is_busy and car.count_passenger_seats >= count_passengers:
                    if not is_baby or (is_baby and car.is_baby_seat):
                        car.is_busy = True
                        return car





car1 = Taxi(7, 1, False, True)
car2 = Taxi(5, 2, True, False)
car3 = Taxi(5, 3, False, True)
car4 = Taxi(3, 4, False, False)
car5 = Taxi(5, 5, True, False)
Car = Taxi([car1, car2, car3, car4, car5])

