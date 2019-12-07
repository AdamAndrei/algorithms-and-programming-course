import json

from domain.Medicine import Medicine
from exception.InvalidMedicineException import InvalidMedicineException


class MedicineRepository:
    def __init__(self, filename):
        self.__medicine_storage = {}
        self.__filename = filename

    def __load_from_file(self):
        try:
            with open(self.__filename, "r") as f_read:
                saved_drugs = json.load(f_read)
                self.__medicine_storage.clear()
                for saved_drug in saved_drugs:
                    drug = Medicine(*saved_drug)
                    self.__medicine_storage[drug.get_id_entity()] = drug
        except FileNotFoundError:
            self.__medicine_storage = {}

    def __save_to_file(self):
        to_save = []
        for medicine in self.__medicine_storage.values():
            found_medicine = [medicine.get_id_entity(),
                              medicine.get_medicine_name(),
                              medicine.get_name_medicine_producer(),
                              medicine.get_medicine_price(),
                              medicine.get_recipe_need()]
            to_save.append(found_medicine)
        with open(self.__filename, "w") as f_write:
            json.dump(to_save, f_write)

    def create(self, drug):
        self.__load_from_file()
        if not isinstance(drug, Medicine):
            raise InvalidMedicineException("This is not a medicine type")
        key = drug.get_id_entity()
        if key in self.__medicine_storage:
            raise InvalidMedicineException("Id {} already exists".format(drug.get_id_entity()))
        self.__medicine_storage[key] = drug
        self.__save_to_file()

    def read_by_id(self, medicine_id):
        self.__load_from_file()
        if medicine_id in self.__medicine_storage:
            return self.__medicine_storage[medicine_id]
        return None

    def read_all(self):
        self.__load_from_file()
        return self.__medicine_storage.values()

    def update(self, medicine):
        self.__load_from_file()
        if not isinstance(medicine, Medicine):
            raise InvalidMedicineException("This is not a medicine type")
        medicine_id = medicine.get_id_entity()
        if medicine_id not in self.__medicine_storage:
            raise InvalidMedicineException("Id {} already exists".format(medicine.get_id_entity()))
        self.__medicine_storage[medicine_id] = medicine
        self.__save_to_file()

    def delete(self, medicine_id):
        self.__load_from_file()
        if medicine_id not in self.__medicine_storage:
            raise InvalidMedicineException("There's no ID = {}".format(medicine_id))
        del self.__medicine_storage[medicine_id]
        self.__save_to_file()


