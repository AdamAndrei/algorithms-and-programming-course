class Medicine:
    def __init__(self, medicine_id, medicine_name, name_medicine_producer, medicine_price, recipe_need):
        self.__medicine_id = medicine_id
        self.__medicine_name = medicine_name
        self.__name_medicine_producer = name_medicine_producer
        self.__medicine_price = medicine_price
        self.__recipe_need = recipe_need

    def __eq__(self, other):
        if not isinstance(other, Medicine):
            return False
        return self.__medicine_id == other.__medicine_id and \
               self.__medicine_name == other.__medicine_name and \
               self.__name_medicine_producer == other.__name_medicine_producer and \
               self.__medicine_price == other.__medicine_price and \
               self.__recipe_need == other.__recipe_need

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "id_medicine = {}, medicine_name = {}, name_medicine_producer = {}, medicine_price = {}," \
               "recipe_need = {}".format(self.__medicine_id,
                                         self.__medicine_name,
                                         self.__name_medicine_producer,
                                         self.__medicine_price,
                                         self.__recipe_need)

    def get_medicine_id(self):
        return self.__medicine_id

    def get_medicine_name(self):
        return self.__medicine_name

    def get_name_medicine_producer(self):
        return self.__name_medicine_producer

    def get_medicine_price(self):
        return self.__medicine_price

    def get_recipe_need(self):
        return self.__recipe_need

    def set_medicine_name(self, new_medicine_name):
        self.__medicine_name = new_medicine_name

    def set_name_medicine_producer(self, new_name_medicine_producer):
        self.__name_medicine_producer = new_name_medicine_producer

    def set_medicine_price(self, new_medicine_price):
        self.__medicine_price = new_medicine_price

    def set_recipe_need(self, new_recipe_need):
        self.__recipe_need = new_recipe_need

    def get_text_format(self):
        return "{},{},{},{},{}".format(self.get_medicine_id(),
                                       self.get_medicine_name(),
                                       self.get_name_medicine_producer(),
                                       self.get_medicine_price(),
                                       self.get_recipe_need())
