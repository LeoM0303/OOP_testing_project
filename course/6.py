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

    def set_bound(self, left):
        self.MIN_COORDS = left


pt1 = Point(1,3)

pt1.set_bound(10)
print(pt1.__dict__)