# Sam Cole
# 11/14/2019


class Car:

    def __init__(self, color, mpg, top_speed):
        self.color = color
        self.mpg = mpg
        self.top_speed = top_speed

    def describe(self):
        return "The color of the car is " + self.color + ", the miles per gallon of the car is " + str(self.mpg) + "," \
            "the top speed of the car is " + str(self.top_speed)
