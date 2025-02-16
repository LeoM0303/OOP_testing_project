class Point:
    def __init__(self, x=0, y=0):
        if self.__check_coards(x) and self.__check_coards(y):
            self.__x = self.__y = 0
            self.__x = x
            self.__x = y

    @classmethod
    def __check_coards(cls, x):
        return type(x) in (int, float)

    def set_coords(self, x,y):
        if self.__check_coards(x) and self.__check_coards(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError

    def get_coords(self):
        return self.__x, self.__y

pt = Point(1,2)
pt.set_coords(3,4)
print(pt.get_coords())