class Point:
    color = 'red'
    circle = 2

    def __init__(self, a, b):
       self.x = a
       self.y = b

    def set_coords(self, x,y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

pt = Point(1,2)
print(pt.__dict__)