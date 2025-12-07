barang_list = [
    {"nomor": 1, "nama": "Rokok", "harga": 30000},
    {"nomor": 2, "nama": "Roti", "harga": 12000},
    {"nomor": 3, "nama": "Minyak", "harga": 17500},
    {"nomor": 4, "nama": "Mie Instan", "harga": 3000},
    {"nomor": 5, "nama": "Odol", "harga": 12000},
    {"nomor": 6, "nama": "Sikat Gigi", "harga": 10000}
]

riwayat = []

def tampilkan_barang():
    print("\nDaftar Barang-barang") 
    for i in barang_list:
        print(f"{i["nomor"]}. {i["nama"]} Rp.{i["harga"]}")
    print("--------------------")

def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            return angka
        except ValueError:
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

def cari_barang():
    kata_kunci = input("Cari: ").lower()
    print("Hasil:")
    for i in barang_list:
        if kata_kunci in i["nama"].lower():
            print(f"{i["nomor"]}. {i["nama"]} Rp.{i["harga"]}")
            print("")
            return 
    print("Maaf, barang tersebut tidak ada\n")    

def transaksi():
    keranjang = []
    total = 0

    while True:
        tampilkan_barang()
        pilih = input("Masukkan nomor barang yang ingin dibeli.\nKetik x jika sudah selesai: ")

        if pilih == "x":
            break
        try:
            pilih = int(pilih)
        except ValueError:
            print("Masukkan angka yang sesuai atau x jika sudah selesai!")
            continue
        ditemukan = False
        for i in barang_list:
            if i["nomor"] == pilih:
                ditemukan = True
                jumlah = input_angka("Jumlah: ")
                subtotal = i["harga"] * jumlah

                keranjang.append(f"{i['nama']} x{jumlah} = Rp.{subtotal}")
                total += subtotal
                print("Ditambahkan")
        if not ditemukan:
            print("Tidak ada barangnya") 
            
    print("Total pembayaran: Rp.", total)
    bayar = input_angka("Uang bayar: Rp. ")
    if bayar < total:
        print("Maaf uangnya kurang kak")
        return
        
    kembalian = bayar - total
    print("Kembalian: Rp.", kembalian)

    struk_belanja = ""
    for i in keranjang:
        struk_belanja += i + "\n"
    struk_belanja += "----------------------\n"
    struk_belanja += "TOTAL BIAYA: Rp." + str(total) + "\n"
    struk_belanja += "----------------------\n"
    struk_belanja += "TUNAI      : Rp." + str(bayar) + "\n"
    struk_belanja += "KEMBALI    : Rp." + str(kembalian) + "\n"
    struk_belanja += "Terima Kasih Sudah Berbelanja Di Warung Mas Limpat!\n"
    struk_belanja += "\n"

    riwayat.append(struk_belanja)

     file = open("riwayat_kasir.txt", "a")
    file.write(struk_belanja)
    file.close()
    print("Transaksi telah disimpan!")
    print("--------------------")





