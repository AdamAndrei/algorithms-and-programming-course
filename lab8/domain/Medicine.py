from domain.Entity import Entity


class Medicine(Entity):
    def __init__(self, medicine_id, medicine_name, name_medicine_producer, medicine_price, recipe_need, is_removed):
        super(Medicine, self).__init__(medicine_id)
        self.__medicine_name = medicine_name
        self.__name_medicine_producer = name_medicine_producer
        self.__medicine_price = medicine_price
        self.__recipe_need = recipe_need
        self.__is_removed = is_removed

    def __eq__(self, other):
        if not isinstance(other, Medicine):
            return False
        return self.get_id_entity() == other.get_id_entity() and \
            self.__medicine_name == other.__medicine_name and \
            self.__name_medicine_producer == other.__name_medicine_producer and \
            self.__medicine_price == other.__medicine_price and \
            self.__recipe_need == other.__recipe_need and \
            self.__is_removed == other.__is_removed

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "id_medicine = {} medicine_name = {} name_medicine_producer = {} medicine_price = {} " \
               "recipe_need = {} is removed = {}".format(self.get_id_entity(),
                                                         self.__medicine_name,
                                                         self.__name_medicine_producer,
                                                         self.__medicine_price,
                                                         self.__recipe_need,
                                                         self.__is_removed)

    def get_medicine_name(self):
        return self.__medicine_name

    def get_name_medicine_producer(self):
        return self.__name_medicine_producer

    def get_medicine_price(self):
        return self.__medicine_price

    def get_recipe_need(self):
        return self.__recipe_need

    def get_is_removed(self):
        return self.__is_removed

    def set_medicine_name(self, new_medicine_name):
        self.__medicine_name = new_medicine_name

    def set_name_medicine_producer(self, new_name_medicine_producer):
        self.__name_medicine_producer = new_name_medicine_producer

    def set_medicine_price(self, new_medicine_price):
        self.__medicine_price = new_medicine_price

    def set_recipe_need(self, new_recipe_need):
        self.__recipe_need = new_recipe_need

    def get_text_format(self):
        return "{},{},{},{},{}".format(self.get_id_entity(),
                                       self.get_medicine_name(),
                                       self.get_name_medicine_producer(),
                                       self.get_medicine_price(),
                                       self.get_recipe_need(),
                                       self.get_is_removed())
