from abc import ABC, abstractmethod

class Menutakjil(ABC):
    @abstractmethod
    def tambahkan(self, menu):
        pass

    @abstractmethod
    def hapus(self,menu):
        pass

class Menusore(Menutakjil):
    def __init__(self, menu):
        self.menu = menu

    def tambahkan(self, menu):
        self.menu.append(menu)
        print(f"{menu}telah ditambagkan.")

    def hapus(self, menu):
        if menu in self.menu:
            self.menu.remove(menu)
            print(f"{menu} telah dihapus.")
        else:
            print(f"{menu} tidak ada dalam daftar bumbu.")

if __name__ == "__main__":
    Menusore = Menutakjil
    print("Daftar menu saat ini:", Menusore.menu)

    Menusore.tambahkan("Kolak")
    Menusore.tambahkan("Es Buah")
    Menusore.tambahkan("Es Teh")
    Menusore.tambahkan("Tahu Goreng")
    Menusore.tambahkan("Es Campur")
    Menusore.tambahkan("Kurma")
    Menusore.tambahkan("Sosis Bakar")
    Menusore.tambahkan("Rujak Buah")
    Menusore.tambahkan("Sate Ayam")
    print("Daftar menu setelah penambahan:", Menusore.menu)

    print("Menu sudah tidak tersedia")
    
    Menusore.hapus("Sate Ayam")
    Menusore.hapus("Es Buah")
    print("Daftar menu setelah penghapusan:", Menusore.menu)

