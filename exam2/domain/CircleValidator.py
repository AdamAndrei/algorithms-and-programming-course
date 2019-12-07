from domain.Circle import Circle
from exceptions.InvalidRadiusException import InvalidRadiusException


class CircleValidator:
    def validate_circle(self, circle: Circle):
        if circle.get_circle_radius() <= 0:
            raise InvalidRadiusException("Radius must be a positive number")
