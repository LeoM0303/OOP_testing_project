class Vector:
    MinCoard = 0
    MaxCoard = 100

    @classmethod
    def get_valid_coards(cls, arg):
        return cls.MinCoard <= arg <= cls.MaxCoard

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.get_valid_coards(x) and self.get_valid_coards(y):
            self.x = x
            self.y = y

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x ** 2 + y ** 2

v = Vector(1,300)
print('Your vectors coardinate: ', v.get_coords())
print('Square + sum : ', Vector.norm2(1,300))