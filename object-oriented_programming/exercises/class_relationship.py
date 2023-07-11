"""
Classes exercise

1st - Create a Car Class
2nd - Create a Engine Class
3rd - Create a Manufacturer Class
4th - Do a connection between Car and Engine

Attention: - The engine can be from several cars

5th - Do a connection between car and manufacturer

Attention: - One manufacturer can produce several cars

Final: show the car, engine and manufacturer name in screen

"""


class Car:
    def __init__(self, car_name):
        self.car_name = car_name
        self._car_engine = None
        self._car_manufac = None
    
    @property
    def car_engine(self):
        return self._car_engine
    
    @car_engine.setter
    def car_engine(self, value):
        self._car_engine = value

    @property
    def car_manufac(self):
        return self._car_manufac

    @car_manufac.setter    
    def car_manufac(self, value):
        self._car_manufac = value

class Engine:
    def __init__(self, name):
        self.name = name

class Manufac:
    def __init__(self, name):
        self.name = name


fusca = Car('Fusca')
volkswagen = Manufac('Volkswagen')
motor_1_0 = Engine('1.0')
fusca.car_manufac = volkswagen
fusca.car_engine = motor_1_0

print(fusca.car_name, fusca.car_manufac.name, fusca.car_engine.name)

SF_90 = Car('SF_90')
Ferrari = Manufac('Ferrari')
motor_4_0 = Engine('4.0')
SF_90.car_manufac = Ferrari
SF_90.car_engine = motor_4_0

print(SF_90.car_name, SF_90.car_manufac.name, SF_90.car_engine.name)
