import string
import math


class Point:

    def set_coordinates(self, *args):
        alphabet = list(string.ascii_lowercase)
        if 26 >= len(args) >= 2:
            for i in range(0, len(args)):
                setattr(self, alphabet[i], args[i])

    def get_distance(self, object):
        if isinstance(object, Point):
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
p2.set_coordinates(4, 6, 7)
print(p2.get_distance(p1))

