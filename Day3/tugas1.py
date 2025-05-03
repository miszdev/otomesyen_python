def is_prima(n):
    """
    Fungsi untuk menentukan apakah suatu bilangan adalah bilangan prima.
    Mengembalikan True jika prima, False jika tidak.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Perulangan untuk mencetak angka 1 hingga 30
for angka in range(1, 31):
    keterangan = ""

    # Tentukan apakah prima terlebih dahulu
    if is_prima(angka):
        keterangan = "Prima"
    else:
        # Tentukan apakah genap atau ganjil jika bukan prima
        if angka % 2 == 0:
            keterangan = "Genap"
        else:
            keterangan = "Ganjil"

    # Cetak angka dan keterangan
    print(f"{angka}: {keterangan}")