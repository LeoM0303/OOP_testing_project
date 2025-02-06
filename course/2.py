class Point:
    color = 'red'
    circle = 2

    def __init__(self):
       print("Calling init")
       self.x = 0
       self.y = 0

    def set_coords(self, x,y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

pt = Point()
print(pt.__dict__)