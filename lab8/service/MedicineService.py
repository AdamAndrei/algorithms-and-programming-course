import random
import string

from domain.Medicine import Medicine
from domain.MedicineValidator import MedicineValidator
from my_tools.my_sorted import my_sorted
from repository.GenericRepository import GenericRepository


class MedicineService:
    def __init__(self,
                 medicine_repository: GenericRepository,
                 medicine_validator: MedicineValidator,
                 transaction_repository: GenericRepository):
        self.__medicine_repository = medicine_repository
        self.__medicine_validator = medicine_validator
        self.__transaction_repository = transaction_repository

    def add_medicine(self,
                     medicine_id,
                     medicine_name,
                     name_medicine_producer,
                     medicine_price,
                     recipe_need,
                     is_removed):
        """
        Creates a medicine
        :param is_removed:
        :param medicine_id:int
        :param medicine_name:  string
        :param name_medicine_producer: string
        :param medicine_price: float
        :param recipe_need: bool
        """
        medicine = Medicine(medicine_id, medicine_name, name_medicine_producer, medicine_price, recipe_need, is_removed)
        self.__medicine_validator.validate_medicine(medicine)
        self.__medicine_repository.create(medicine)

    def update_medicine(self,
                        new_medicine_id,
                        new_medicine_name,
                        new_name_medicine_producer,
                        new_medicine_price,
                        new_recipe_need,
                        new_is_removed):
        """
        Update a Medicine object
        :param new_is_removed:
        :param new_medicine_id: int
        :param new_medicine_name: string
        :param new_name_medicine_producer: string
        :param new_medicine_price: float
        :param new_recipe_need: bool
        """
        medicine = Medicine(new_medicine_id, new_medicine_name, new_name_medicine_producer, new_medicine_price,
                            new_recipe_need, new_is_removed)
        self.__medicine_validator.validate_medicine(medicine)
        self.__medicine_repository.update(medicine)

    def get_list_of_drugs_that_match(self, the_string):
        """
        Finds all thew drugs that contains the given string into them
        :param the_string: string
        :return: a list of drugs
        """
        found_medicine = []
        for medicine in self.__medicine_repository.read_all():
            if the_string in medicine.get_text_format():
                found_medicine.append(medicine)
        return found_medicine

    def get_all_drugs(self):
        """

        :return: a list of drugs
        """
        found_drugs = []
        for medicine in self.__medicine_repository.read_all():
            found_drugs.append(medicine)
        return found_drugs

    def get_drug(self, id_drug):
        return self.__medicine_repository.read_by_id(id_drug)

    def get_medicines_id_in_descending_order_by_pieces_number(self):
        """

        :return: list of drugs in descending order bu the amount of the pieces
        """
        list_of_drugs = self.__medicine_repository.read_all()
        max_per_id = {}
        for transaction in self.__transaction_repository.read_all():
            medicine_id_in_transaction = transaction.get_medicine_transacted_id()
            pieces_number_for_medicine = transaction.get_pieces_number()
            if medicine_id_in_transaction not in max_per_id:
                max_per_id[medicine_id_in_transaction] = 0
            max_per_id[medicine_id_in_transaction] += pieces_number_for_medicine
        # list_of_filtered_drugs = []
        # for drug in list_of_drugs:
        #     if drug.get_id_entity() in max_per_id:
        #         list_of_filtered_drugs.append(drug)
        # for index in range(len(list_of_filtered_drugs) - 1):
        #     for k in range(index, len(list_of_filtered_drugs)):
        #         drug_index = list_of_filtered_drugs[index]
        #         drug_k = list_of_filtered_drugs[k]
        #         if max_per_id[drug_index.get_id_entity()] < max_per_id[drug_k.get_id_entity()]:
        #             list_of_filtered_drugs[index] = drug_k
        #             list_of_filtered_drugs[k] = drug_index
        list_of_filtered_drugs = list(filter(lambda medicine: medicine.get_id_entity() in max_per_id, list_of_drugs))
        final_list = my_sorted(list_of_filtered_drugs,
                               key=lambda medicine: max_per_id[medicine.get_id_entity()], reverse=True)
        list_of_pieces_number = []
        for drug in final_list:
            list_of_pieces_number.append(max_per_id[drug.get_id_entity()])
        list_of_drugs_and_number_of_pieces = zip(final_list, list_of_pieces_number)
        return list_of_drugs_and_number_of_pieces

    def expensive_medicine(self, percentage, maximum_price):
        """
        Expense the price of the drugs with the price smaller than the price given
        :param percentage: float
        :param maximum_price: float
        """
        list_of_medicines = self.__medicine_repository.read_all()
        # for drug in list_of_medicines:
        #     if drug.get_medicine_price() < maximum_price:
        #         self.__do_expense(drug, percentage)
        self.__expensive_medicine_recursive(percentage, maximum_price, list_of_medicines)

    def __do_expense(self, drug, percentage):
        expense_price = drug.get_medicine_price() * (1 + percentage / 100)
        new_id = drug.get_id_entity()
        new_name = drug.get_medicine_name()
        new_producer_name = drug.get_name_medicine_producer()
        new_recipe_need = drug.get_recipe_need()
        is_removed = drug.get_is_removed()
        self.update_medicine(new_id, new_name, new_producer_name, expense_price, new_recipe_need, is_removed)

    def __expensive_medicine_recursive(self, percentage, max_price, list_of_medicines):
        if not list_of_medicines:
            return
        first_drug = list_of_medicines[0]
        if first_drug.get_medicine_price() < max_price:
            self.__do_expense(first_drug, percentage)
        self.__expensive_medicine_recursive(percentage, max_price, list_of_medicines[1:])


    def populate(self, n):
        """
        Creates n Medicine objects
        :param n: int
        :return: list of all medicines from storage
        """
        list_of_id = []
        for medicine in self.__medicine_repository.read_all():
            medicine_id = medicine.get_id_entity()
            list_of_id.append(medicine_id)
        sorted_list = sorted(list_of_id)
        start_id = sorted_list[-1] + 1
        letters = string.ascii_letters
        for index in range(n):
            medicine_name = ''.join(random.choice(letters) for i in range(15))
            medicine_producer_name = ''.join(random.choice(letters) for i in range(25))
            medicine_price = float(random.randint(0, 1000))
            recipe_need = random.choice([True, False])
            is_removed = random.choice([True, False])
            medicine = Medicine(start_id, medicine_name, medicine_producer_name, medicine_price,
                                recipe_need, is_removed)
            self.__medicine_validator.validate_medicine(medicine)
            self.add_medicine(start_id, medicine_name, medicine_producer_name, medicine_price, recipe_need, is_removed)
            start_id += 1
        # while n != 0:
        #     medicine_name = ''.join(random.choice(letters) for i in range(15))
        #     medicine_producer_name = ''.join(random.choice(letters) for i in range(25))
        #     medicine_price = float(random.randint(0, 1000))
        #     recipe_need = random.choice([True, False])
        #     is_removed = random.choice([True, False])
        #     medicine = Medicine(start_id, medicine_name, medicine_producer_name, medicine_price,
        #                         recipe_need, is_removed)
        #     self.__medicine_validator.validate_medicine(medicine)
        #     self.add_medicine(start_id, medicine_name, medicine_producer_name, medicine_price,
        #     recipe_need, is_removed)
        #     start_id += 1
        #     n -= 1
        return self.__medicine_repository.read_all()

    def delete_medicine_and_transactions(self, id_medicine):
        medicine = self.__medicine_repository.read_by_id(id_medicine)
        medicine_name = medicine.get_medicine_name()
        medicine_producer_name = medicine.get_name_medicine_producer()
        medicine_price = medicine.get_medicine_price()
        recipe_need = medicine.get_recipe_need()
        self.update_medicine(id_medicine, medicine_name, medicine_producer_name, medicine_price, recipe_need, True)
        for transaction in self.__transaction_repository.read_all():
            if transaction.get_medicine_transacted_id() == id_medicine:
                self.__transaction_repository.delete(transaction.get_id_entity())

    def remove_medicine(self, id_medicine):
        self.__medicine_repository.delete(id_medicine)
