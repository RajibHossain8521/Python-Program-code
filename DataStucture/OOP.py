class Vehicle:
    """ Base class for all vehicles """

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def turn(self, direction):
        print('Turning', self.name, 'to', direction)


class Car(Vehicle):
    """ Car class inherit the Base class'Vehicle' """

    def __init__(self, name, manufacturer, color, year):
        super().__init__(name, manufacturer, color)
        self.year = 2017
        self.wheels = 4

    def change_gear(self, gear_name):
        """ Method of changing hear """
        print('Changing gear', self.name, 'to', gear_name)

    # override the base class method and this is call Method overriding

    def turn(self, direction):
        print(self.name, 'turning to', direction)


if __name__ == '__main__':
    c = Car("Mustang 5.0 GT coupe", "Ford", "Red", 2017)
    v = Vehicle("Harrier", "Toyota", "White")
    c.turn("right")
    v.turn("Left")

