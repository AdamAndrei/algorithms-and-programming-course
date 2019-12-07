from domain.CircleValidator import CircleValidator
from repository.GenericRepository import GenericRepository
from service.CircleService import CircleService
from user_interface.Console2 import Console


def main():
    circle_validator = CircleValidator()
    circle_repository = GenericRepository("circle.pickle")
    circle_service = CircleService(circle_repository, circle_validator)
    ui = Console(circle_service)
    ui.run_console()


main()
