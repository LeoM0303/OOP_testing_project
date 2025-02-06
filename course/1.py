class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x,y):
        self.x = x
        self.y = y


pt = Point()
pt.set_coords(1,2)
print(pt.__dict__)

pt2 = Point()
pt2.set_coords(10,20)
print(pt2.__dict__)