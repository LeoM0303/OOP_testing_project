##for market create OOP style


def main() -> None:
    dataset = get_information()
    if dataset is None:
        return

    name_product, location = dataset
    print(f"Product: {name_product.capitalize()}, Location: {location.capitalize()}")

def get_information() -> tuple[str, str] | None:
    while True:
        name_product = input("Enter name of product: ").strip()
        location = input("Enter location: ").strip()
        if not name_product or not location:
            print("Invalid input")
            return None

        return name_product, location

if __name__ == "__main__":
    main()
