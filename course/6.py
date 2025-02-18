class Point:
    MAX_COORDS = 1000
    MIN_COORDS = 0


    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        if self.MIN_COORDS <= x <= self.MAX_COORDS and self.MIN_COORDS <= y <= self.MAX_COORDS:
            self.x = x
            self.y = y

    def __gettributte__(self, item):
        print('Get attribute: ')
        return object.__getattribute__(self, item)

pt1 = Point(1,2)
pt2 = Point(1000,2000)

a = pt1.x
print(a)