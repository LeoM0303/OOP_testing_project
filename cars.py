from typing import Optional

class Car:
    def __init__(self, make, model):
        self.make = make.strip()
        self.model = model.strip()

    def __str__(self) -> str:
        print(f"Make: {self.make} | Model: {self.model}")

    @classmethod
    def get_car_information(cls) -> Optional["Car"]:
        name = cls._get_valid_input("Enter your name: ")
        model = cls._get_valid_input("Enter model: ")

        return cls(name, model)


    @staticmethod
    def _get_valid_input(prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("You did not enter a name, please try again")


def main() -> None:
    car = Car.get_car_information()
    if car:
        print(car.__str__())

if __name__ == "__main__":
    main()