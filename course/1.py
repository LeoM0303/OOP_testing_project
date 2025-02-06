class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x,y):
        self.x = x
        self.y = y

pt = Point()
pt.set_coords(1,2)
print(pt.__dict__)