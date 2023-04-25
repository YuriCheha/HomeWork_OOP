# наземный транспорт(стать такси, self.taxi=True, taxi=False)
# ,водный транспорт(военный корабль или нет),
# добавить метод плыть, метод всплыть, метод спуститься на дно
# Вертолет(пилот, количество мест, команда),
# машина(тип двигателя, коробка передач), лодка(капитан)

# И создать экземпляры каждого класса.

from abc import ABC, abstractmethod
class Transport():
    engine: str
    model: str
    mileage: int
    color: str
    max_velocity: int
    def __init__(self, engine,model, mileage, color, max_velocity):
        self.engine = engine
        self.model = model
        self.millage = mileage
        self.color = color
        self.max_velocity = max_velocity
        print('Создали транспорт')

    def start(self):
        print("Start")
    def stop(self):
        print("Stop")

class AirTransport(Transport):

    def __init__(self, engine, model, mileage, color, max_velocity, seats, max_height, chassis, wings):
        super().__init__(engine, model, mileage, color, max_velocity)
        self.seats = seats
        self.max_height = max_height
        self.chassis = chassis
        self.wings = wings

    def fly(self):
        print("Воздух - Воздух!!!")


class GroundTransport(Transport):
    def __init__(self, engine, model, mileage, color, max_velocity, taxi):
        super().__init__(engine, model, mileage, color, max_velocity)
        self.taxi = taxi

        def taxi_(self):
            if self.taxi == taxi:
                print('Taxi')
            else:
                print('Не такси')

class WaterTransport(Transport):
    def __init__(self, engine, model, mileage, color, max_velocity, military):
        super().__init__(engine, model, mileage, color, max_velocity)
        self.military = military

    def swim(self):
        print("Начинаем движение")
    def down(self):
        print("Погружение")
    def surface(self):
        print("Всплыть")


a1 = AirTransport('бензин', "БМВ", "100500", "красный", "200км/ч", "3", "1500", "3", "10")
b1 = GroundTransport('бензин', "БМВ", "100500", "красный", "200км/ч", "3")
c1 = WaterTransport('бензин', "БМВ", "100500", "красный", "200км/ч", "3")
print(c1)