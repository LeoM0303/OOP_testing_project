class DataBase:
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
