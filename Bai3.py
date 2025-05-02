import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        self.__x, self.__y = map(int, input().split())

    def print(self):
        print(f"({self.__x}, {self.__y})", end="")

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def distance(self, other=None):
        if other is None:
            return math.sqrt(self.__x ** 2 + self.__y ** 2)
        else:
            return math.sqrt((self.__x - other.getX()) ** 2 + (self.__y - other.getY()) ** 2)

class ColorPoint(Point):
    def __init__(self, x=0, y=1, color="xanh"):
        super().__init__(x, y)
        self.__color = color

    def read(self):
        super().read()
        self.__color = input().strip()

    def print(self):
        super().print()
        print(f": {self.__color}")

    def setColor(self, color):
        self.__color = color

class C002454:
    @staticmethod
    def testCase1():
        A = ColorPoint(5, 10, "trắng")
        A.print()

    @staticmethod
    def testCase2():
        B = ColorPoint()
        B.read()
        B.move(10, 8)
        B.print()

    @staticmethod
    def testCase3():
        C = ColorPoint(6, 3, "đen")
        D = ColorPoint(C.getX(), C.getY(), C._ColorPoint__color)  # Truy cập thuộc tính private
        D.print()
        D.setColor("vàng")
        D.print()
        C.print()

    @staticmethod
    def main():
        C002454.testCase1()
        C002454.testCase2()
        C002454.testCase3()

# Chạy chương trình
if __name__ == "__main__":
    C002454.main()        