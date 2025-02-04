from typing import Optional

class Person:
    def __init__(self, name, age):
        self._name = name.strip().capitalize()
        self._age = age

    @classmethod
    def get_information(cls) -> Optional["Person"]:
        name = cls._get_valid_input("Enter your name: ")
        age = cls._get_valid_age("Enter your age: ")

        return cls(name, age)

    @staticmethod
    def _get_valid_input(prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("You did not enter a name, please try again")

    @staticmethod
    def _get_valid_age(prompt: str) -> int:
        while True:
            value = input(prompt).strip()
            if value.isdigit() and int(value) > 0:
                return int(value)
            print("You did not enter the age correctly, try again")

    def __str__(self) -> str:
        return f"Name: {self._name} | Age: {self._age}"

def main() -> None:
        person = Person.get_information()
        if person:
            print(person)

if __name__ == "__main__":
    main()