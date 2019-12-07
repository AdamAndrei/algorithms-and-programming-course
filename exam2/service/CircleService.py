import math
# import turtle
import turtle

from domain.Circle import Circle
from domain.CircleValidator import CircleValidator
from repository.GenericRepository import GenericRepository


class CircleService:
    def __init__(self, circle_repository: GenericRepository, circle_validator: CircleValidator):
        self.__circle_repository = circle_repository
        self.__circle_validator = circle_validator

    def add_circle(self, circle_id, abscissa, ordinate, radius):
        circle = Circle(circle_id, abscissa, ordinate, radius)
        self.__circle_validator.validate_circle(circle)
        self.__circle_repository.create(circle)

    def update_circle(self, circle_id, new_abscissa, new_ordinate, new_radius):
        circle = Circle(circle_id, new_abscissa, new_ordinate, new_radius)
        self.__circle_validator.validate_circle(circle)
        self.__circle_repository.update(circle)

    def remove_circle(self, circle_id):
        self.__circle_repository.delete(circle_id)

    def read_by_id(self, circle_id):
        return self.__circle_repository.read_by_id(circle_id)

    def read_all(self):
        found_circle = []
        for circle in self.__circle_repository.read_all():
            found_circle.append(circle)
        return found_circle

    @staticmethod
    def calculate_area(circle: Circle):
        area = circle.get_circle_radius() ** 2
        return area

    def get_all_circles_area(self):
        area_per_id = {}
        for circle in self.__circle_repository.read_all():
            area_per_id[circle.get_id_entity()] = CircleService.calculate_area(circle)
        return area_per_id

    def get_circles_in_descending_order_by_area(self):
        areas = self.get_all_circles_area()
        list_of_circles = self.__circle_repository.read_all()
        return sorted(list_of_circles, key=lambda circle: areas[circle.get_id_entity()], reverse=True)

    @staticmethod
    def distance_between_two_points(x, y, a, b):
        return math.sqrt(((x - a) ** 2) + ((y - b) ** 2))

    def get_all_circles_that_contain_one_point(self, a, b):
        found_circles = []
        for circle in self.__circle_repository.read_all():
            abscissa = circle.get_circle_abscissa()
            ordinate = circle.get_circle_ordinate()
            radius = circle.get_circle_radius()
            if CircleService.distance_between_two_points(abscissa, ordinate, a, b) == radius:
                found_circles.append(circle)
        return found_circles

    def remove_circles_with_some_radius(self, a, b):
        for circle in self.__circle_repository.read_all():
            radius = circle.get_circle_radius()
            circle_id = circle.get_id_entity()
            if a < b:
                if a <= radius <= b:
                    self.__circle_repository.delete(circle_id)
            if a > b:
                if b <= radius <= a:
                    self.__circle_repository.delete(circle_id)
            if a == b:
                if radius == a:
                    self.__circle_repository.delete(circle_id)

    def get_biggest_and_smallest_radius(self):
        list_of_extremes = []
        list_of_radius = []
        for circle in self.__circle_repository.read_all():
            list_of_radius.append(circle.get_circle_radius())
        max_radius = max(list_of_radius)
        min_radius = min(list_of_radius)
        list_of_extremes.append(min_radius)
        list_of_extremes.append(max_radius)
        return list_of_extremes

    def draw_the_circles(self):
        list = self.get_biggest_and_smallest_radius()
        min_radius = list[0]
        max_radius = list[1]
        t = turtle.Turtle()
        t.fillcolor('orange')
        t.begin_fill()
        t.circle(min_radius)
        t.end_fill()
        t.fillcolor('blue')
        t.begin_fill()
        t.circle(max_radius)
        t.end_fill()
        t.circle(min_radius)

