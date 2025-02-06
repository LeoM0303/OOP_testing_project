class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user=None, psw=None, port=None):
        if not hasattr(self, 'user'):
            self.user = user
            self.psw = psw
            self.port = port

    def connect(self):
        print(f'Connect with DataBase: user: {self.user} psw: {self.psw} port: {self.port}')

    def close(self):
        print('Close connection')

    def read(self):
        print('Read data')

    def write(self, data):
        print(f'Write in data {data}')


# Приклад використання
dp = DataBase('root', 'helloworld', 80)
dp2 = DataBase('root2', 'helloworld1', 40)
print(id(dp), id(dp2))
dp.connect()
dp2.connect()