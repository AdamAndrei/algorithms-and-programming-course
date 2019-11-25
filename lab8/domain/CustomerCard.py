class CustomerCard:
    def __init__(self, customer_card_id, customer_name, customer_first_name, customer_cnp, birth_date,
                 registration_date):
        self.__customer_card_id = customer_card_id
        self.__customer_name = customer_name
        self.__customer_first_name = customer_first_name
        self.__customer_cnp = customer_cnp
        self.__birth_date = birth_date
        self.__registration_date = registration_date

    def __eq__(self, other):
        if not isinstance(other, CustomerCard):
            return False
        return self.__customer_card_id == other.__customer_card_id and \
            self.__customer_name == other.__customer_name and \
            self.__customer_first_name == other.__customer_first_name and \
            self.__customer_cnp == other.__customer_cnp and \
            self.__birth_date == other.__birth_date and \
            self.__registration_date == other.__registration_date

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "id_customer_card = {}, customer_name = {}, customer_first_name = {}, customer_cnp = {}," \
               " birth_date = {}, registration_date = {}".format(self.__customer_card_id,
                                                                 self.__customer_name,
                                                                 self.__customer_first_name,
                                                                 self.__customer_cnp,
                                                                 self.__birth_date,
                                                                 self.__registration_date)

    def get_customer_card_id(self):
        return self.__customer_card_id

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

    def set_customer_name(self, new_customer_name):
        self.__customer_name = new_customer_name

    def set_customer_first_name(self, new_customer_first_name):
        self.__customer_first_name = new_customer_first_name

    def set_birth_date(self, new_birth_date):
        self.__birth_date = new_birth_date

    def set_registration_date(self, new_registration_date):
        self.__registration_date = new_registration_date

    def get_text_format(self):
        return "{},{},{},{},{},{}".format(self.get_customer_card_id(),
                                          self.get_customer_name(),
                                          self.get_customer_first_name(),
                                          self.get_customer_cnp(),
                                          self.get_birth_date(),
                                          self.get_registration_date())
