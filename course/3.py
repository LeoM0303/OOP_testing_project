class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.user = user()
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Conect with DataBase: user: {self.user} psw: {self.psw} port: {self.port}')

    def close(self):
        print('Close connection')

    def read(self):
        print('Read data')

    def write(self):
        print(f'Write in data {data}')
