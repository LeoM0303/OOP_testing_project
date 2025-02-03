def main() -> None:
    dataset = get_information()
    product, location = dataset

    if not product or not location:
        print("No information found")
        return

    print(f"Products {product} are located at {location.capitalize()}")

def get_information() -> tuple[str, str]:
    while True:
        product = input("Enter product name: ")
        if not product:
            print("Product name cannot be empty")
            continue

        location = input("Enter product location: ")
        if not location:
            print("Product location cannot be empty")
            continue

        return product, location

if __name__ =="__main__":
    main()