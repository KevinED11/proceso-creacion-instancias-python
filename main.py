from typing import Self
import logging


logging.basicConfig(
    filename="main.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class Person(object):
    """
    Creates a new instance of the Persona class.
    """

    def __new__(cls, *args, **kwargs) -> "Person":
        logging.info("Creando una nueva persona.")

        print("Nueva instancia de persona creada.")
        return super().__new__(cls)

    def __init__(self, name: str, age: int, surname: str) -> None:
        self.name = name
        self.age = age
        self.surname = surname

    def __repr__(self) -> str:
        name = self.name
        age = self.age
        return f"{type(self).__name__}({name=}, {age=})"


Person.__name__ = "NewPerson"
print(Person.__name__)


persons: list[Person] = [
    Person("kevin", 22, "KevinED11"),
    Person("alberto", 22, "AlbertoED11"),
]


def find_person(surname: str) -> Person:
    """
    Find a person with the given surname.
    """
    return list(filter(lambda p: p.surname == surname, persons))[0]


def main() -> None:
    print(find_person(surname="KevinED11"))


if __name__ == "__main__":
    main()
    print("Fin del programa.")