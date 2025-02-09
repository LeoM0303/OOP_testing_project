class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, users=None, password=None, port=None):
        if not hasattr(self, 'users'):
            self.users = input("Enter users: ")
            self.password = input("Enter password: ")
            self.port = input("Enter port: ")

    def connect(self):
        print(f'Connect to database: users={self.users.capitalize()}, password={self.password}, port={self.port}')

    def close(self):
        print(f'Close connection')

    def read(self):
        print(f'Read data')

    def write(self):
        print(f'Write data')

db = DataBase()
db2 = DataBase()

db.connect()
db2.connect()

print(id(db), id(db2))
