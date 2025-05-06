import json

class TuLanh:
    def __init__(self, nhanhieu="Elextrolux", maso="UNKNOWN", nuocsx="Việt Nam", tkdien=True, dungtich=256, gia=7000000):
        self.__nhanhieu = nhanhieu
        self.__maso = maso
        self.__nuocsx = nuocsx
        self.__tkdien = tkdien
        self.__dungtich = dungtich
        self.__gia = gia

    def __copy__(self):
        return TuLanh(self.__nhanhieu, self.__maso, self.__nuocsx, self.__tkdien, self.__dungtich, self.__gia)

    def makeCopy(self, tl):
        self.__nhanhieu = tl.__nhanhieu
        self.__maso = tl.__maso
        self.__nuocsx = tl.__nuocsx
        self.__tkdien = tl.__tkdien
        self.__dungtich = tl.__dungtich
        self.__gia = tl.__gia

    def nhapThongTin(self):
        self.__nhanhieu = input().strip()
        self.__maso = input().strip()
        self.__nuocsx = input().strip()
        self.__tkdien = input().strip().lower() == 'true'
        self.__dungtich = int(input().strip())
        self.__gia = int(input().strip())

    def hienThi(self):
        print(f"Nhãn hiệu: {self.__nhanhieu}")
        print(f"Mã số: {self.__maso}")
        print(f"Nước SX: {self.__nuocsx}")
        print(f"T/K điện: {'Có' if self.__tkdien else 'Không'}")
        print(f"Dung tích: {self.__dungtich}L")
        print(f"Giá: {self.__gia:,}VNĐ")

    def layNhanHieu(self):
        return self.__nhanhieu

    def layGia(self):
        return self.__gia

    def soNguoiSD(self):
        return self.__dungtich // 100

    def cungNhanHieu(self, tl):
        return self.__nhanhieu == tl.__nhanhieu

    def nhHon(self, tl):
        return self.__dungtich < tl.__dungtich

    def to_dict(self):
        return {
            "nhanhieu": self.__nhanhieu,
            "maso": self.__maso,
            "nuocsx": self.__nuocsx,
            "tkdien": self.__tkdien,
            "dungtich": self.__dungtich,
            "gia": self.__gia
        }


class C002454:
    def testCase1(self):
        print("Nhập thông tin tủ lạnh tl1:")
        tl1 = TuLanh()
        tl1.nhapThongTin()
        print("\nThông tin tủ lạnh tl2:")
        tl2 = TuLanh("LG", "LG-28382", "Hàn Quốc", True, 600, 43000000)
        tl2.hienThi()
        tl3 = tl1.__copy__()
        tl3.hienThi()

    def testCase2(self):
        n = int(input())
        danhsach = []
        for _ in range(n):
            tlanh = TuLanh()
            tlanh.nhapThongTin()
            danhsach.append(tlanh)
        
        print("\nDanh sách tủ lạnh theo thứ tự ngược:")
        for tlanh in reversed(danhsach):
            tlanh.hienThi()

    def testCase3(self):
        n = int(input())
        danhsach = []
        for _ in range(n):
            tlanh = TuLanh()
            tlanh.nhapThongTin()
            danhsach.append(tlanh)
        
        danhsach.sort(key=lambda x: x.layGia(), reverse=True)
        print("\nDanh sách tủ lạnh theo giá giảm dần:")
        for tlanh in danhsach:
            tlanh.hienThi()

    def testCase4(self):
        n = int(input())
        danhsach = []
        for _ in range(n):
            tlanh = TuLanh()
            tlanh.nhapThongTin()
            danhsach.append(tlanh)
        
        with open("DsTuLanh.json", "w", encoding="utf-8") as f:
            json.dump([tlanh.to_dict() for tlanh in danhsach], f, ensure_ascii=False, indent=4)
        print("\nĐã lưu danh sách vào file DsTuLanh.json")

    def testCase5(self):
        n = int(input())
        danhsach = []
        for _ in range(n):
            tlanh = TuLanh()
            tlanh.nhapThongTin()
            danhsach.append(tlanh)
        
        dem = {}
        for tlanh in danhsach:
            nhan = tlanh.layNhanHieu()
            dem[nhan] = dem.get(nhan, 0) + 1
        
        print("\nThống kê số lượng theo nhãn hiệu:")
        for nhan in sorted(dem.keys()):
            print(f"{nhan} ({dem[nhan]})")

    def main(self):
        while True:
            print("\nMENU")
            print("1.testCase1")
            print("2.testCase2")
            print("3.testCase3")
            print("4.testCase4")
            print("5.testCase5")
            print("6.Thoát chương trình")
            choice = input("Chọn chức năng: ")

            if choice == "1":
                self.testCase1()
            elif choice == "2":
                self.testCase2()
            elif choice == "3":
                self.testCase3()
            elif choice == "4":
                self.testCase4()
            elif choice == "5":
                self.testCase5()
            elif choice == "6":
                print("Thoát")
                break
            else:
                print("Error!!!")


if __name__ == "__main__":
    test = C002454()
    test.main()