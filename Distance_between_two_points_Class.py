import math


class Point:

    def set_coordinates(self, *args):
        if len(args) >= 2:
            for i in range(0, len(args)):
                setattr(self, str(i), args[i])
        else:
            print("Переданы неверные координаты")

    def get_distance(self, object):

        if isinstance(object, Point) and len(self.__dict__.values()) == len(object.__dict__.values()):
            dist_array1 = [int(i) for i in self.__dict__.values()]
            dist_array2 = [int(i) for i in object.__dict__.values()]
            dist = 0
            for i in range(len(dist_array1)):
                dist += math.pow(dist_array2[i] - dist_array1[i], 2)
            return math.sqrt(dist)
        else:
            print("Передана не точка")


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2, 8)
p2.set_coordinates(4, 6, 9)
print(p2.get_distance(p1))

