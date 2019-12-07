from domain.CustomerCard import CustomerCard
from exception.InvalidCNPException import InvalidCNPException
from exception.InvalidCustomerCardException import InvalidCustomerCardException


class CustomerCardValidator:
    @staticmethod
    def validate_customer_card(customer_card: CustomerCard):
        """
        Function verify if an object respects some conditions and if it finds an irregularity raise an exception
        :param customer_card: an CustomerCard object
        :return: exceptions
        """
        if not isinstance(customer_card.get_id_entity(), int):
            raise InvalidCustomerCardException("ID = {} must be an int".format(customer_card.get_id_entity()))
        if len("{}".format(customer_card.get_customer_cnp())) != 13:
            raise InvalidCNPException("CNP {} must be made out of 13"
                                      " characters".format(customer_card.get_customer_cnp()))
        if len("{}".format(customer_card.get_customer_name())) == 0:
            raise InvalidCustomerCardException("Customer has to get a name ")
        if len("{}".format(customer_card.get_customer_first_name())) == 0:
            raise InvalidCustomerCardException("Customer has to get a name ")
        if not isinstance(customer_card.get_customer_cnp(), int):
            raise InvalidCustomerCardException("CNP {} must be int".format(customer_card.get_customer_cnp()))
        if "/" not in customer_card.get_birth_date():
            raise InvalidCustomerCardException("please use / for writing date")
        if "/" not in customer_card.get_registration_date():
            raise InvalidCustomerCardException("please use / for writing date")
        if len("{}".format(customer_card.get_birth_date())) < 5:
            raise InvalidCustomerCardException("Date is not valid")
        if len("{}".format(customer_card.get_registration_date())) < 5:
            raise InvalidCustomerCardException("Date is not valid")
        birth_date = customer_card.get_birth_date().split(sep="/")
        if len(birth_date) != 3:
            raise InvalidCustomerCardException("Use only two /")
        if int(birth_date[0]) < 1 or int(birth_date[0]) > 31:
            raise InvalidCustomerCardException("Day {} must be between 1 and 31".format(int(birth_date[0])))
        if int(birth_date[1]) < 1 or int(birth_date[1]) > 12:
            raise InvalidCustomerCardException("Month {} must be between 1 and 12".format(int(birth_date[1])))
        if int(birth_date[2]) > 2019:
            raise InvalidCustomerCardException("Year cannot be in the future {}".format(int(birth_date[2])))
        registration_date = customer_card.get_registration_date().split(sep="/")
        if int(registration_date[0]) < 1 or int(registration_date[0]) > 31:
            raise InvalidCustomerCardException("Day {} must be between 1 and 31".format(int(registration_date[0])))
        if int(registration_date[1]) < 1 or int(registration_date[1]) > 12:
            raise InvalidCustomerCardException("Month {} must be between 1 and 12".format(int(registration_date[1])))
        if int(registration_date[2]) > 2019:
            raise InvalidCustomerCardException("Year cannot be in the future {}".format(int(registration_date[2])))
        if len(registration_date) != 3:
            raise InvalidCustomerCardException("Use only two /")

    @staticmethod
    def validate_date(date):
        """
        Function verify if a date id valid
        :param date: string
        :return: raise exceptions if the date doesn't respect some conditions
        """
        date = date.split(sep="/")
        if len(date) != 3:
            raise InvalidCustomerCardException("Use only 2 /")
        if int(date[0]) < 1 or int(date[0]) > 31:
            raise InvalidCustomerCardException("Day {} must be between 1 and 31".format(int(date[0])))
        if int(date[1]) < 1 or int(date[1]) > 12:
            raise InvalidCustomerCardException("Month {} must be between 1 and 12".format(int(date[1])))
        if int(date[2]) > 2019:
            raise InvalidCustomerCardException("Year {} cannot be in the future".format(int(date[2])))
