import json

from lab8.exception.InvalidIdException import InvalidIdException


class GenericRepository:
    def __init__(self, filename):
        self.__storage = {}
        self.__filename = filename

    def __load_from_file(self):
        try:
            with open(self.__filename, "r") as f_read:
                self.__storage.clear()
        except FileNotFoundError:
            self.__storage = {}

    def __save_to_file(self):
        with open(self.__filename, "w") as f_write:
            json.dump(self.__storage, f_write)

    def create(self, entity):
        self.__load_from_file()
        id_entity = entity.id_entity
        if id_entity in self.__storage:
            raise InvalidIdException('The entity id already exists!')
        self.__storage[id_entity] = entity
        self.__save_to_file()

    def read(self, id_entity=None):
        self.__load_from_file()
        if id_entity is None:
            return self.__storage.values()

        if id_entity in self.__storage:
            return self.__storage[id_entity]
        return None

    def update(self, entity):
        self.__load_from_file()
        id_entity = entity.id_entity
        if id_entity not in self.__storage:
            raise InvalidIdException('There is no entity with that id!')
        self.__storage[id_entity] = entity
        self.__save_to_file()

    def delete(self, id_entity):
        self.__load_from_file()
        if id_entity not in self.__storage:
            raise InvalidIdException('There is no entity with that id!')
        del self.__storage[id_entity]
        self.__save_to_file()
