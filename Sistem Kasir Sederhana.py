barang_list = [
    {"nomor": 1, "nama": "Air Minum", "harga": 5000},
    {"nomor": 2, "nama": "Roti", "harga": 12000},
    {"nomor": 3, "nama": "Cookie", "harga": 15000},
    {"nomor": 4, "nama": "Es Krim", "harga": 3500},
    {"nomor": 5, "nama": "Mie Instan", "harga": 5000},
    {"nomor": 6, "nama": "Galon", "harga": 50000},
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

def tambah_barang():
    while True:
        nama = input("Nama barang: ")
        if nama.strip() == "":
            print("Nama tidak boleh kosong!")
        else:
            harga = input_angka("Harga barang: Rp.")
            if harga > 0:
                nomor_baru = len(barang_list) + 1
                barang_list.append({"nomor": nomor_baru, "nama": nama, "harga": harga})
                print("Barang telah ditambahkan!")
                print("--------------------")
                break
            else:
                print("Nominal harga harus diatas 0!\n")

def edit_hapus_barang():
    tampilkan_barang()
    pilih = input_angka("Nomor barang yang dipilih: ")
    for i in barang_list:
        if i["nomor"] == pilih:
            print("1. Edit")
            print("2. Hapus")
            aksi = input("Pilih: ")

            while True:
                if aksi == "1":
                    while True:
                        nama_baru = input("Nama baru: ")
                        if nama_baru.strip() == "":
                            print("Nama tidak boleh kosong!")
                        else:
                            i["nama"] = nama_baru
                            break
                    while True:
                        harga_baru = input_angka("Harga baru: Rp.")
                        if harga_baru <= 0:
                            print("Nominal harga harus diatas 0!")
                        else:
                            i["harga"] = harga_baru
                            print("Barang telah diperbarui!\n")
                            break

                    break
                elif aksi == "2":
                    barang_list.remove(i)
                    print("Barang telah dihapus!\n")
                    break
                else:
                    print("Aksi tidak valid!\n")
                    return
            
            return
    print("Barang tidak ditemukan!\n")
