##for market create OOP style


def main() -> None:
    dataset = get_information()
    name_product, location = dataset

    if not name_product or not location:
        print("Invalid input")

    print(f"Product: {name_product.capitalize()}, Location: {location.capitalize()}")

def get_information() -> tuple[str, str]:
    while True:
        name_product = input("Enter name of product: ")
        if not name_product:
            print("Invalid input")
            continue

        location = input("Enter location: ")
        if not location:
            print("Invalid input")
            continue

        return name_product, location

if __name__ == "__main__":
    main()
