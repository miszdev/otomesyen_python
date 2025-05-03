class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary  # Confidential attribute

    def show_info(self):
        print(f"Nama: {self.name}")
        print(f"Posisi: {self.position}")
        print("Gaji: Confidential")

    def raise_salary(self):
        if self.position.lower() == "it":
            self.__salary *= 1.10
        elif self.position.lower() == "hr":
            self.__salary *= 1.15
        elif self.position.lower() == "direktur":
            self.__salary *= 1.01
        else:
            print("Posisi tidak dikenali untuk kenaikan gaji.")
        print(f"Gaji {self.name} telah diperbarui.")

    def get_salary(self):
        return self.__salary