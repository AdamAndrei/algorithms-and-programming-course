from domain.Medicine import Medicine
from exception.InvalidMedicineException import InvalidMedicineException


class MedicineValidator:
    @staticmethod
    def validate_medicine(medicine: Medicine):
        """
        Function verify if an object respects some conditions and if it finds an irregularity raise an exception
        :param medicine: an Medicine object
        :return: exceptions
        """
        if not isinstance(medicine.get_id_entity(), int):
            raise InvalidMedicineException("Medicine id {} is not int".format(medicine.get_id_entity()))
        if not isinstance(medicine.get_medicine_price(), float):
            raise InvalidMedicineException("Medicine price {} is not float".format(medicine.get_medicine_price()))
        if not isinstance(medicine.get_recipe_need(), bool):
            raise InvalidMedicineException("Recipe need {} must be True or False".format(medicine.get_recipe_need()))
        if medicine.get_medicine_price() <= 0:
            raise InvalidMedicineException("Medicine price {} must be a positive "
                                           "number".format(medicine.get_medicine_price()))
        if len("{}".format(medicine.get_medicine_name())) == 0:
            raise InvalidMedicineException("Medicine has to get a name ")
        if len("{}".format(medicine.get_name_medicine_producer())) == 0:
            raise InvalidMedicineException("Producer has to get a name ")
