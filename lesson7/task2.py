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


class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool, is_busy: bool, car_numb: int):
        self.color = color
        self.seat = count_passenger_seats
        self.b_seat = is_baby_seat
        self.busy = is_busy
        self.car_numb = car_numb

    # def __str__(self):
    #     return (f"цвет={self.color}, "
    #             f"количество поссажирских мест={self.seat}, "
    #             f"детское кресло={self.b_seat}"
    #             f"")


car_1 = Car(color="красный", count_passenger_seats=7, is_baby_seat=False, is_busy=False, car_numb=1)
car_2 = Car(color="синий", count_passenger_seats=7, is_baby_seat=True, is_busy=False, car_numb=2)


class Taxi:

    def __init__(self, cars: list[Car]):
        self.cars = cars

    def find_car(self, count_passenger_seats, is_baby_seat):
        for car in self.cars:
            # if car.is_busy is False and car.count_passenger_seats >= count_p:
            #     if is_b is False or (is_b is True and car.is_baby_seat is True):
            car.is_busy = True
            print("ok")
