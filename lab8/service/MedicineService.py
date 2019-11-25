import copy
import random
import string

from lab8.domain.Medicine import Medicine
from lab8.domain.MedicineValidator import MedicineValidator
from lab8.repository.MedicineRepository import MedicineRepository
from lab8.repository.TransactionRepository import TransactionRepository


class MedicineService:
    def __init__(self,
                 medicine_repository: MedicineRepository,
                 medicine_validator: MedicineValidator,
                 transaction_repository:TransactionRepository):
        self.__medicine_repository = medicine_repository
        self.__medicine_validator = medicine_validator
        self.__transaction_repository = transaction_repository

    def add_medicine(self,
                     medicine_id,
                     medicine_name,
                     name_medicine_producer,
                     medicine_price,
                     recipe_need):
        medicine = Medicine(medicine_id, medicine_name, name_medicine_producer, medicine_price, recipe_need)
        self.__medicine_validator.validate_medicine(medicine)
        self.__medicine_repository.create(medicine)

    def update_medicine(self,
                        new_medicine_id,
                        new_medicine_name,
                        new_name_medicine_producer,
                        new_medicine_price,
                        new_recipe_need):
        medicine = Medicine(new_medicine_id, new_medicine_name, new_name_medicine_producer, new_medicine_price,
                            new_recipe_need)
        self.__medicine_validator.validate_medicine(medicine)
        self.__medicine_repository.update(medicine)

    def get_list_of_drugs_that_match(self, the_string):
        found_medicine = []
        for medicine in self.__medicine_repository.read_all():
            if the_string in medicine.get_text_format():
                found_medicine.append(medicine)
        return found_medicine

    def get_all_drugs(self):
        found_drugs = []
        for medicine in self.__medicine_repository.read_all():
            found_drugs.append(medicine)
        return found_drugs

    def get_medicines_id_in_descending_order_by_pieces_number(self):
        list_of_drugs = self.__medicine_repository.read_all()
        max_per_id = {}
        for transaction in self.__transaction_repository.read_all():
            medicine_id_in_transaction = transaction.get_medicine_transacted_id()
            pieces_number_for_medicine = transaction.get_pieces_number()
            if medicine_id_in_transaction not in max_per_id:
                max_per_id[medicine_id_in_transaction] = 0
            max_per_id[medicine_id_in_transaction] += pieces_number_for_medicine
        list_of_filtered_drugs = []
        for drug in list_of_drugs:
            if drug.get_medicine_id() in max_per_id:
                list_of_filtered_drugs.append(drug)
        for index in range(len(list_of_filtered_drugs) - 1):
            for k in range(index, len(list_of_filtered_drugs)):
                drug_index = list_of_filtered_drugs[index]
                drug_k = list_of_filtered_drugs[k]
                if max_per_id[drug_index.get_medicine_id()] < max_per_id[drug_k.get_medicine_id()]:
                    list_of_filtered_drugs[index] = drug_k
                    list_of_filtered_drugs[k] = drug_index
        return list_of_filtered_drugs

    def expensive_medicine(self, percentage, maximum_price):
        list_of_medicines = self.__medicine_repository.read_all()
        for drug in list_of_medicines:
            if drug.get_medicine_price() < maximum_price:
                expense_price = drug.get_medicine_price() * (1 + percentage / 100)
                new_id = drug.get_medicine_id()
                new_name = drug.get_medicine_name()
                new_producer_name = drug.get_name_medicine_producer()
                new_recipe_need = drug.get_recipe_need()
                self.update_medicine(new_id, new_name, new_producer_name, expense_price, new_recipe_need)

    def populate(self, n):
        list_of_id = []
        for medicine in self.__medicine_repository.read_all():
            medicine_id = medicine.get_medicine_id()
            list_of_id.append(medicine_id)
        sorted_list = sorted(list_of_id)
        start_id = sorted_list[-1] + 1
        letters = string.ascii_letters
        for index in range(n):
            medicine_name = ''.join(random.choice(letters) for i in range(15))
            medicine_producer_name = ''.join(random.choice(letters) for i in range(25))
            medicine_price = float(random.randint(0, 1000))
            recipe_need = random.choice([True, False])
            medicine = Medicine(start_id, medicine_name, medicine_producer_name, medicine_price, recipe_need)
            self.__medicine_validator.validate_medicine(medicine)
            self.add_medicine(start_id, medicine_name, medicine_producer_name, medicine_price, recipe_need)
            start_id += 1
        return self.__medicine_repository.read_all()