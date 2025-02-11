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

v = Vector(1,2)
print(v.get_coords())
