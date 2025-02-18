class Cat:
    breed = 'pers'

    def hello(*args):
        print("Hello!")

    def show_breed(instance):
        print(f'my breed is {instance.breed}')

