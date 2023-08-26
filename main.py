from typing import Self
class Persona:
    def __new__(cls, *args, **kwargs) -> object:
        print("Nueva instancia de persona creada.")
        return super().__new__(cls)

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        name = self.name
        age = self.age
        return f"{type(self).__name__}({name=}, {age=})"


kevin = Persona(name="kevin", age=22)
print(kevin)