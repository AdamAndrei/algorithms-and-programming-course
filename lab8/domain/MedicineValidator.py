from lab8.domain.Medicine import Medicine


class MedicineValidator:

    def validate_medicine(self, medicine: Medicine):
        if not isinstance(medicine.get_medicine_id(), int):
            raise ValueError("Medicine id {} is not int".format(medicine.get_medicine_id()))
        if not isinstance(medicine.get_medicine_price(), float):
            raise ValueError("Medicine price {} is not float".format(medicine.get_medicine_price()))
        if not isinstance(medicine.get_recipe_need(), bool):
            raise ValueError("Recipe need {} must be True or False".format(medicine.get_recipe_need()))
        if medicine.get_medicine_price() <= 0:
            raise ValueError("Medicine price {} must be a positive "
                             "number".format(medicine.get_medicine_price()))
        if len("{}".format(medicine.get_medicine_name())) == 0:
            raise ValueError("Medicine has to get a name ")
        if len("{}".format(medicine.get_name_medicine_producer())) == 0:
            raise ValueError("Producer has to get a name ")
