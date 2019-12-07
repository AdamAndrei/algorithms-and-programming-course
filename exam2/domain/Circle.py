from domain.EntityThree import Entity


class Circle(Entity):
    def __init__(self, circle_id, circle_abscissa, circle_ordinate, radius):
        super(Circle, self).__init__(circle_id)
        self.__circle_abscissa = circle_abscissa
        self.__circle_ordinate = circle_ordinate
        self.__radius = radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return self.get_id_entity() == other.get_id_entity() and \
               self.__circle_abscissa == other.__circle_abscissa and \
               self.__circle_ordinate == other.__circle_ordinate and \
               self.__radius == other.__radius

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "Circle id = {}  circle abscissa = {}  circle ordinate = {}" \
               " circle radius = {}".format(self.get_id_entity(),
                                            self.__circle_abscissa,
                                            self.__circle_ordinate,
                                            self.__radius)

    def get_circle_id(self):
        return self.get_id_entity()

    def get_circle_abscissa(self):
        return self.__circle_abscissa

    def get_circle_ordinate(self):
        return self.__circle_ordinate

    def get_circle_radius(self):
        return self.__radius
