# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле
class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool, is_busy:bool):
        self.color = color
        self.seat = count_passenger_seats
        self.b_seat = is_baby_seat
        self.busy = is_busy
    def __str__(self):
        return (f"цвет={self.color}, "
                f"количество поссажирских мест={self.seat}, "
                f"детское кресло={self.b_seat}"
                f"")

car_1 = Car(color="красный", count_passenger_seats=7, is_baby_seat=True, is_busy=False)
print(car_1)
