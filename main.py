"""
El proceso de creación de instancias de python consta de 2 pasos.
1. Crear una clase
2. Crear una instancia

de manera interna, el proceso de creación de instancias de python se divide en 2 pasos
donde lso constructores activan el proceso de creación de instancias.
1. __new__ -> Crea una nueva instancia de la clase.
2. __init__ -> inicializa la instancia dandole un estado inicial.

dentro de __new__ puedes personalizar el proceso de creación de instancias y tener un
control de mas bajo nivel sobre la creación de instancias.
"""
from typing import Self
import logging
import timeit


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
        return super().__new__(cls) # solo acepta un argumento, la clase a instanciar.

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


class Singleton:
    """
    Creates and returns a new instance of the Singleton class if one does not already exist
    """
    __instance: Self | None = None

    def __new__(cls, *args, **kwargs) -> "Singleton":
        if cls.__instance is None:
            logging.info("Creando una nueva instancia de singleton.")
            cls.__instance = super().__new__(cls)
        return cls.__instance


def main() -> None:
    print(find_person(surname="KevinED11"))

    first = Singleton()
    second = Singleton()
    print(first is second)


time1 = timeit.timeit('[*"kevin"]', number=100000)
time2 = timeit.timeit('list("alber")', number=100000)
print(time1), print(time2)


if __name__ == "__main__":
    main()
    print("Fin del programa.")
