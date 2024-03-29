from domain.Entity import Entity


class CustomerCard(Entity):
    def __init__(self, customer_card_id, customer_name, customer_first_name, customer_cnp, birth_date,
                 registration_date, is_removed):
        super(CustomerCard, self).__init__(customer_card_id)
        self.__customer_name = customer_name
        self.__customer_first_name = customer_first_name
        self.__customer_cnp = customer_cnp
        self.__birth_date = birth_date
        self.__registration_date = registration_date
        self.__is_removed = is_removed

    def __eq__(self, other):
        if not isinstance(other, CustomerCard):
            return False
        return self.get_id_entity() == other.get_id_entity() and \
            self.__customer_name == other.__customer_name and \
            self.__customer_first_name == other.__customer_first_name and \
            self.__customer_cnp == other.__customer_cnp and \
            self.__birth_date == other.__birth_date and \
            self.__registration_date == other.__registration_date and \
            self.__is_removed == other.__is_removed

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "id_customer_card = {} customer_name = {} customer_first_name = {} customer_cnp = {}" \
               " birth_date = {} registration_date = {} is removed = {}".format(self.get_id_entity(),
                                                                                self.__customer_name,
                                                                                self.__customer_first_name,
                                                                                self.__customer_cnp,
                                                                                self.__birth_date,
                                                                                self.__registration_date,
                                                                                self.__is_removed)

    def get_customer_name(self):
        return self.__customer_name

    def get_customer_first_name(self):
        return self.__customer_first_name

    def get_customer_cnp(self):
        return self.__customer_cnp

    def get_birth_date(self):
        return self.__birth_date

    def get_registration_date(self):
        return self.__registration_date

    def get_is_removed_card(self):
        return self.__is_removed

    def set_customer_name(self, new_customer_name):
        self.__customer_name = new_customer_name

    def set_customer_first_name(self, new_customer_first_name):
        self.__customer_first_name = new_customer_first_name

    def set_birth_date(self, new_birth_date):
        self.__birth_date = new_birth_date

    def set_registration_date(self, new_registration_date):
        self.__registration_date = new_registration_date

    def get_text_format(self):
        return "{},{},{},{},{},{}".format(self.get_id_entity(),
                                          self.get_customer_name(),
                                          self.get_customer_first_name(),
                                          self.get_customer_cnp(),
                                          self.get_birth_date(),
                                          self.get_registration_date(),
                                          self.get_is_removed_card())
