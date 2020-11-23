# Membuka dan mau membaca file d:/data.txt
try:
    file = open('d:/data.txt', 'r')

# Baca baris pertama dari file
# Simpan ke dalam variabel bil1 sebagai integer
    bil1 = int(file.readline())

# Baca baris pertama dari file
# Simpan ke dalam variabel bil2 sebagai integer
    bil2 = int(file.readline())

# Hitung dan tampilkan hasil bagi
    hasil = bil1/bil2
    print(bil1, 'dibagi' , bil2, ' sama dengan ' , hasil)
except ZeroDivisionError:
    print('Tidak boleh pembagian dengan nol')
except FileNotFoundError:
    print('File tidak di temukan')
