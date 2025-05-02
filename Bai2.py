from Bai1 import Point
import math

class LineSegment:
    __d1 = Point()
    __d2 = Point()
    def __init__(self,*args):
        if len(args) == 0:
            self.__d1 = Point(8,5)
            self.__d2 = Point(1,0)
        if len(args)== 2:
            if not(isinstance(args[0],Point) and isinstance(args[1],Point)):
                raise TypeError("Nhap diem!!!")
            self.__d1 = args[0]
            self.__d2 = args[1]
        if len(args)==4:
            if not all(isinstance(item,int) for item in args):
                raise TypeError("Only Intergers can be added")
            self.__d1 = Point(args[0],args[1])
            self.__d2 = Point(args[2],args[3])
        if len(args)== 1:
            if not isinstance(args[0],LineSegment):
                raise TypeError("Only one LineSegment can be added")
            self.__d1 = Point(args[0].__d1.getX(),args[0].__d1.getY())
            self.__d2 = Point(args[0].__d2.getX(),args[0].__d2.getY())

    def read(self):
        while True:
            try:
                s = input("Nhap vao doan thang (dinh dang: x1 y1 x2 y2): ")
                parts = s.split()
                if len(parts) != 4:
                    raise ValueError("Phai nhap dung 4 gia tri (x1 y1 x2 y2)!")
                self.__d1 = Point(int(parts[0]), int(parts[1]))
                self.__d2 = Point(int(parts[2]), int(parts[3]))
                break  # Thoát khỏi vòng lặp nếu nhập đúng
            except ValueError as e:
                print(f"Loi: {e}. Vui long nhap lai!")
            except IndexError:
                print("Loi: Khong du gia tri. Vui long nhap lai!")
    def __str__(self):
        return "[({},{}); ({},{})]".format(self.__d1.getX(),self.__d1.getY(),self.__d2.getX(),self.__d2.getY())
    def move(self,dx,dy):
        self.__d1.move(dx,dy)
        self.__d2.move(dx,dy)
    def length(self):
        return self.__d1.distance(self.__d2)
    def angle(self):
        dx = self.__d2.getX() - self.__d1.getX()
        dy = self.__d2.getY() - self.__d1.getY()
        return int(math.degrees(math.atan2(dy, dx)))
        
class LineSegmentTest:
    def testCase1(self):
        A = Point(2,5)
        B = Point(20,35)
        AB = LineSegment(A,B)
        print(AB)
        AB.move(35,51)
        print(AB)
    def testCase2(self):
        CD= LineSegment()
        print("|CD| = {:.2f}".format(CD.length()))
    def testCase3(self):
        danhsach = []
        n = int(input("Nhap n: "))
        for i in range (n):
            l1 = LineSegment()
            l1.read()
            danhsach.append(l1)
            

        for item in danhsach:
            print(item)
            print(item.length())
            
        danhsach.sort(key = lambda dist: dist.length())
        for item in danhsach:
            print(item)
            print(item.length())
    
    def main(self):
        while True:
            s=input("Nhap kich ban muon chay 1/2/3/exit: ")
            if s == '1':
                LineSegmentTest().testCase1()
            if s == '2':
                LineSegmentTest().testCase2()
            if s=='3':
                LineSegmentTest().testCase3()
            if s=='exit':
                break
                
        
LineSegmentTest().main()