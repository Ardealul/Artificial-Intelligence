from random import randint


class Ant:
    def __init__(self, params=None):
        self.__solution = [randint(1, params['noNodes'])]
        self.__distance = 0

    @property
    def solution(self):
        return self.__solution

    @property
    def distance(self):
        return self.__distance

    @solution.setter
    def solution(self, l=[]):
        self.__solution = l

    @distance.setter
    def distance(self, distance):
        self.__distance = distance

    def __str__(self):
        return "\nAnt: " + str(self.__solution) + " with cost: " + str(self.__distance)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, a):
        return self.__solution == a.__solution and self.__distance == a.__distance




