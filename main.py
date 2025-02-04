from typing import Optional

class Market:
    def __init__(self, name: str, price: int, motherland: str) -> None:
        self.name = name.strip().capitalize()
        self.price = price
        self.motherland = motherland.strip().capitalize()

    @classmethod
    def get_information(cls) -> Optional["Market"]:
        name = cls._get_valid_input("Enter name of product: ")
        price = cls._get_valid_price("Enter price of product: ")
        motherland = cls._get_valid_input("Enter motherland of product: ")

        return cls(name, price, motherland)

    @staticmethod
    def _get_valid_input(prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Input can't be empty! Please try again.")

    @staticmethod
    def _get_valid_price(prompt: str) -> int:
        while True:
            value = input(prompt).strip()
            if value.isdigit() and int(value) > 0:
                return int(value)
            print("Invalid price! Enter a positive number.")

    def __str__(self) -> str:
        return f"Market: {self.name} | Price: ${self.price} | Motherland: {self.motherland}"


def main() -> None:
    market = Market.get_information()
    if market:
        print(market)


if __name__ == "__main__":
    main()
