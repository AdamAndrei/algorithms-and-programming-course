from lab7.domain.Item import Item
from lab7.exeption.InvalidItemException import InvalidItemException
from lab7.repository.ItemRepository import ItemRepository


class ItemValidator:
    def __init__(self, item_repository: ItemRepository):
        self.__item_repository = item_repository

    def validate(self, item: Item):
        if not isinstance(item.get_id(), int):
            raise InvalidItemException("ID '{}' is not int".format(item.get_id()))
        if not isinstance(item.get_price(), int):
            raise InvalidItemException("name '{}' is not int".format(item.get_price()))
        if item.get_description() == "":
            raise InvalidItemException("Description must not be null")
        if item.get_name() == "":
            raise InvalidItemException("Name must not be null")


    # def __validate_unique_id(self, item: Item):
    #     if self.__item_repository.exists(item.get_id()):
    #         raise InvalidItemException("ID must be unique")
