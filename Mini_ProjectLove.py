import json 

data_keuangan = {
     "saldo" : 0,
     "riwayat_transaksi" : []
}

try: 
     with open ("Keuangan.json","r") as file:
          data_keuangan = json.load(file)

except FileNotFoundError:
     with open ("Keuangan.json","w") as file :
          json.dump(data_keuangan, file, indent=4)
          print("File Belum Ada")

except json.JSONDecodeError:
     print("Format JSON Tidak Valid")

     data_keuangan = {
          "saldo" : 0,
          "riwayat_transaksi" : []

     }

     with open ("Keuangan.json","w") as file :
          json.dump(data_keuangan, file, indent=4)

saldo = data_keuangan["saldo"]
riwayat_transaksi = data_keuangan["riwayat_transaksi"]

def tambah_saldo(saldo, pemasukan) :
    return saldo + pemasukan

def tarik_saldo(saldo, penarikan) :
    return saldo - penarikan

def tampil_saldo(saldo) :
     print("\n\n===== PERSONAL FINANCE TRACKER ===== ")
     print("\nSaldo Anda : Rp." , saldo)
     print("\n1. Tambah Pemasukan ")
     print("2. Tarik Saldo ")
     print("3. Lihat Saldo ")
     print("4. Riwayat Transaksi ") 
     print("5. Total Pemasukan ")
     print("6. Total Pengeluaran ")
     print("7. Hitung Selisih ")
     print("8. Tampilkan Laporan Keuangan ")
     print("9. Reset Data ") 
     print("10. Keluar ") 

def tampil_riwayat_transaksi(riwayat_transaksi, saldo) :
     print("\n\n ===== RIWAYAT TRANSAKSI =====")
     if not riwayat_transaksi :
        print("\nRiwayat Kosong")
     else:
        for nomor, transaksi in enumerate (riwayat_transaksi, start=1):
            if transaksi ["jenis"] == "pemasukan":
                print(nomor,"Uang Masuk :", transaksi["jumlah"])
            
            elif transaksi["jenis"] == "penarikan":
                 print(nomor ,"Uang Keluar :", transaksi["jumlah"])
        print("Saldo Anda Saat Ini : Rp.", saldo)

def hitung_total_pemasukan (riwayat_transaksi):
     total = 0 

     for transaksi in riwayat_transaksi :
          if transaksi ["jenis"] == "pemasukan":
               total += transaksi ["jumlah"]

     return total

def hitung_total_pengeluaran (riwayat_transaksi):
     total = 0

     for transaksi in riwayat_transaksi :
          if transaksi ["jenis"] == "penarikan":
               total += transaksi ["jumlah"]

     return total 

def hitung_selisih(total_pemasukan, total_pengeluaran):
     return total_pemasukan - total_pengeluaran

def tampilkan_laporan(saldo , riwayat_transaksi):
    total_pemasukan = hitung_total_pemasukan(riwayat_transaksi)
    total_pengeluaran = hitung_total_pengeluaran(riwayat_transaksi)

    selisih = hitung_selisih(total_pemasukan, total_pengeluaran)

    print("\n===== LAPORAN KEUANGAN =====")
    print("Saldo Saat Ini      : Rp.", saldo)
    print("Total Pemasukan     : Rp.", total_pemasukan)
    print("Total Pengeluaran   : Rp.", total_pengeluaran)
    print("Selisih             : Rp.", selisih)

def reset_data():
     return 0, [] 

def simpan_data(saldo, riwayat_transaksi):
     data_keuangan = {
          "saldo" : saldo,
          "riwayat_transaksi" : riwayat_transaksi
     }

     with open ("Keuangan.json","w") as file:
          json.dump(data_keuangan, file, indent=4)

while True :

    try : 
        
        tampil_saldo(saldo)

        nilai = int(input("Pilih Menu : "))

        if nilai == 1 :

             try : 

                  pemasukan = float(input("Masukkan Pemasukan : Rp. "))
                  if pemasukan <= 0 :
                       print("Pemasukan Harus Lebih Besar Dari Nol")
                       continue
                  
                  saldo = tambah_saldo(saldo, pemasukan)
                  print("Saldo Berhasil Ditambahkan")
                  transaksi = {
                       "jenis" : "pemasukan" ,
                       "jumlah": pemasukan 
                  }
                  riwayat_transaksi.append(transaksi)
                  simpan_data(saldo, riwayat_transaksi)

             except ValueError :
                  print("Pemasukan Harus Angka !") 

        elif nilai == 2 :

            try :

                 penarikan = float(input("Masukkan Jumlah Penarikan : Rp. "))
                 if penarikan > saldo or penarikan <= 0 :
                      print("Penarikan Harus Lebih Dari 0 Dan Tidak Boleh Melebihi Saldo")
                      continue
                 
                 saldo = tarik_saldo(saldo, penarikan)
                 print("Penarikan Uang Berhasil")
                 transaksi = {
                                "jenis" : "penarikan" ,
                                "jumlah": penarikan 
                                   }
                 riwayat_transaksi.append(transaksi)
                 simpan_data(saldo, riwayat_transaksi)

            except ValueError :
                 print("Penarikan Harus Angka !")

        elif nilai == 3 :
             print("Saldo Saat Ini : Rp. ", saldo)

        elif nilai == 4 :
             tampil_riwayat_transaksi(riwayat_transaksi , saldo)

        elif nilai == 5 :
             print("\nTotal Pemasukan : Rp. ",hitung_total_pemasukan (riwayat_transaksi)) 

        elif nilai == 6 :
             print("\nTotal Pengeluaran : Rp. ",hitung_total_pengeluaran(riwayat_transaksi))

        elif nilai == 7 :
             total_pemasukan = hitung_total_pemasukan(riwayat_transaksi)
             total_pengeluaran = hitung_total_pengeluaran(riwayat_transaksi)
             print("Selisih : Rp. ", hitung_selisih(total_pemasukan, total_pengeluaran))

        elif nilai == 8 :
             tampilkan_laporan(saldo, riwayat_transaksi)
             
        elif nilai == 9 :
            konfirmasi = input("Data Akan Reset ? Tekan Y/N : ").lower()

            if konfirmasi == "y"  :
                saldo, riwayat_transaksi = reset_data()
                simpan_data(saldo, riwayat_transaksi)
                print("\nReset Data berhasil")

            elif konfirmasi == "n" :
                 print("\nReset Data Batal")

            else :
                 print("\nInput Tidak Valid")
               
        elif nilai == 10 :
            print("Terima Kasih")
            break

        else : 
             print("Pilihan Tidak Ada Omm")

    except ValueError : 
        print("Harus Memasukkan Pilihan Angka")

#Project Personal Finace Tracker
#Menambahkan Komentar
#Belajar Git