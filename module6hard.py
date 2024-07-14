from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *side, fill=True):
        self.__sides = [*side]
        self.__color = [*color]
        self.filled = fill


    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    @staticmethod
    def __is_valid_color(*args):
        for i in args:
            if not isinstance(i, int) or not 0 <= i <= 255:
                return False
        return True

    def is_valid_sides_count(self, args):
        if len(args) != self.sides_count:
            args = (1,) * self.sides_count
        return args  # tuple returned

    def __is_valid_sides(self, *args):
        for i in args:
            if not isinstance(i, int) or not len(args) == self.sides_count:
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *sides): 

        if self.__is_valid_sides(*sides):
            self.__sides = [*sides]

    def __len__(self):
        return sum(self.get_sides())


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *side):
        super().__init__(color, *self.is_valid_sides_count(side))
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *side):
        super().__init__(color, *self.is_valid_sides_count(side))
        self.__height = [self.sides_count ** 0.5 / 2 * i for i in self.get_sides()]

    def get_height(self, side=0):
        return self.__height[side]

    def get_square(self):
        return self.get_height() * self.get_sides()[0] / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *side):
        super().__init__(color, *self.is_valid_sides_count((side) * self.sides_count))

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)  #
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())

