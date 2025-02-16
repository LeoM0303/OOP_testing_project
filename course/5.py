class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__x = y

    def set_coords(self, x,y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y

pt = Point(1,2)
pt.set_coords(3,4)
print(pt.get_coords())