from abc import ABC, abstractmethod

class Menutakjil(ABC):
    @abstractmethod
    def tambahkan(self, menu):
        pass

    @abstractmethod
    def hapus(self, menu):
        pass

class Menusore(Menutakjil):
    def __init__(self):
        self.menu = []

    def tambahkan(self, menu):
        self.menu.append(menu)
        print(f"- {menu.ljust(12)} =  telah ditambahkan.")


    def hapus(self, menu):
        if menu in self.menu:
            self.menu.remove(menu)
            print(f"{menu} telah dihapus.")
        else:
            print(f"- {menu.ljust(12)} =  tidak ada dalam daftar.")

if __name__ == "__main__":
    menusore = Menusore()
    print("Daftar menu saat ini:")
    print("\n".join(menusore.menu))

    menusore.tambahkan("Kolak")
    menusore.tambahkan("Es Buah")
    menusore.tambahkan("Es Teh")
    menusore.tambahkan("Tahu Goreng")
    menusore.tambahkan("Es Campur")
    menusore.tambahkan("Kurma")
    menusore.tambahkan("Sosis Bakar")
    menusore.tambahkan("Rujak Buah")
    menusore.tambahkan("Sate Ayam")
    
    print("\nDaftar menu setelah penambahan:")
    print("\n".join("- " + menu for menu in menusore.menu))

    print("\nMenu sudah tidak tersedia :")
    
    menusore.hapus("- Sate Ayam")
    menusore.hapus("- Es Buah")

    print("\nDaftar menu setelah penghapusan:")
    print("\n".join("- " + menu for menu in menusore.menu))

