list_barang = [
    {"nomor": 1, "nama": "Air Minum", "harga": 5000},
    {"nomor": 2, "nama": "Roti", "harga": 12000},
    {"nomor": 3, "nama": "Cookie", "harga": 15000},
    {"nomor": 4, "nama": "Es Krim", "harga": 3500},
    {"nomor": 5, "nama": "Mie Instan", "harga": 5000},
    {"nomor": 6, "nama": "Galon", "harga": 50000}
    {"nomor": 7, "nama": "Rokok", "harga": 30000},
    {"nomor": 8, "nama": "Terminal colokan", "harga": 15000},
    {"nomor": 9, "nama": "Minyak", "harga": 20000},
    {"nomor": 10, "nama": "Odol", "harga": 12000},
    {"nomor": 11, "nama": "Sikat Gigi", "harga": 10000}
]

riwayat = []

def tampilkan_barang():
    print("\nDaftar Barang-barang") 
    for i in barang_list:
        print(i["nomor"], i["nama"], i["harga"])
    print("--------------------")

def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            return angka
        except:
            print("Masukkan angka yang benar!") 