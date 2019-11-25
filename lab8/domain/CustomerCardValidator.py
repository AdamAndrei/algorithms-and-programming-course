from lab8.domain.CustomerCard import CustomerCard
from lab8.exception.InvalidCNPException import InvalidCNPException
from lab8.exception.InvalidCustomerCardException import InvalidCustomerCardException


class CustomerCardValidator:
    def validate_customer_card(self, customer_card: CustomerCard):
        if not isinstance(customer_card.get_customer_card_id(), int):
            raise InvalidCustomerCardException("ID = {} must be an int".format(customer_card.get_customer_card_id()))
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
