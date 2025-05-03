from source import Employee

POSITIONS = {
    "1": "IT",
    "2": "HR",
    "3": "Direktur"
}

def add_employee():
    name = input("Masukkan nama karyawan: ")

    print("Pilih posisi karyawan:")
    for key, value in POSITIONS.items():
        print(f"{key}. {value}")
    position_choice = input("Masukkan nomor posisi: ")

    position = POSITIONS.get(position_choice)
    if not position:
        print("Pilihan posisi tidak valid.")
        return None

    try:
        salary = float(input("Masukkan gaji karyawan: "))
    except ValueError:
        print("Input gaji tidak valid. Harap masukkan angka.")
        return None

    return Employee(name, position, salary)

def main():
    print("Selamat datang di Sistem Karyawan\n")

    emp1 = Employee("Indra", "IT", 10000000)
    emp2 = Employee("Hari", "HR", 8000000)
    emp3 = Employee("Uno", "Direktur", 25000000)

    employees = [emp1, emp2, emp3]

    while True:
        print("\nMenu Utama:")
        print("1. Lihat Daftar Karyawan")
        print("2. Pilih Karyawan")
        print("3. Tambah Karyawan Baru")
        print("4. Keluar")

        menu_choice = input("Pilih menu: ")

        if menu_choice == "1":
            print("\nDaftar Karyawan:")
            for i, employee in enumerate(employees, 1):
                print(f"{i}. {employee.name} - {employee.position}")

        elif menu_choice == "2":
            if not employees:
                print("Tidak ada karyawan tersedia.")
                continue

            print("\nPilih karyawan:")
            for i, employee in enumerate(employees, 1):
                print(f"{i}. {employee.name} - {employee.position}")
            choice = input("Pilih berdasarkan nomor: ")

            if not choice.isdigit() or int(choice) not in range(1, len(employees)+1):
                print("Pilihan tidak valid.")
                continue

            selected = employees[int(choice)-1]
            print(f"\nTerpilih: {selected.name}")
            print("1. Tampilkan Info")
            print("2. Naikkan Gaji")
            print("3. Tampilkan Gaji Sekarang")
            action = input("Pilih aksi: ")

            if action == "1":
                selected.show_info()
            elif action == "2":
                selected.raise_salary()
            elif action == "3":
                print(f"Gaji Sekarang: Rp{selected.get_salary():,.0f}")
            else:
                print("Aksi tidak valid.")

        elif menu_choice == "3":
            new_employee = add_employee()
            if new_employee:
                employees.append(new_employee)
                print(f"Karyawan '{new_employee.name}' telah ditambahkan.")

        elif menu_choice == "4":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan menu tidak valid.")

if __name__ == "__main__":
    main()