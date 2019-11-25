class Item:
    def __init__(self, ID, name, description, price, location):
        self.__ID = ID
        self.__name = name
        self.__description = description
        self.__price = price
        self.__location = location

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.__ID == other.__ID and self.__name == other.__name and self.__description == other.__description and self.__price == other.__price and self.__location == other.__location

    def __ne__(self, other):
        return not(self == other)

    def __str__(self) -> str:
        return "ID={}, name={}, desc={}, price={}, loc={}".format(self.__ID, self.__name, self.__description, self.__price, self.__location)

    def get_id(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_location(self):
        return self.__location

    def set_name(self, new_name):
        self.__name = new_name

    def set_description(self, new_description):
        self.__description = new_description

    def set_price(self, new_price):
        self.__price = new_price

    def set_location(self, new_location):
        self.__location = new_location

