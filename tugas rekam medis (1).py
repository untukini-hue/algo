#Program Rekam Medis
#I.S :
#F.S :
import os

#KONSTANTA
MAKSDATA = 100

#subrutin menampilkan data Rekam Medis dalam bentuk tabel
def TampilRekamMedis(N ,Nama, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    print('                                             DAFTAR REKAM MEDIS')
    print('                                             ------------------')
    print('------------------------------------------------------------------------------------------------------------------------------------------------')
    print('|  No  |      Nama Pasien      | Jenis Kelamin |     Keluhan     | Tekanan Darah | Denyut Nadi | Suhu | Saturasi Oksigen | Tanggal\Bulan\Tahun |')
    print('------------------------------------------------------------------------------------------------------------------------------------------------')
    for i in range(N):
        print(f'| {i+1:>4} | {Nama[i]:>21} | {JK[i]:>10} | {Keluhan[i]:>15} | {TD[i]:^13} | {DN[i]:^11} | {Suhu[i]:^4} | {SO[i]:^16} | {Tanggal[i]:7}\{Bulan[i]:5}\{Tahun[i]:5} |')
    print('------------------------------------------------------------------------------------------------------------------------------------------------')
    
#subrutin menu pilihan
def MenuPilihan(Menu):
    os.system('cls')
    print("<<MENU PILIHAN>>")
    print("1. Isi Data Rekam Medis")
    print("2. Tampil Data Rekam Medis")
    print("3. Tambah Data Rekam Medis")
    print("4. Hapus Data Rekam Medis")
    print("5. Urut Data Rekam Medis")
    print("6. Cari Data Rekam Medis")
    print("7. Penghancuran Data Rekam Medis")
    print("0. Keluar")
    Menu = int(input("Pilihan Anda? "))
    return Menu
 
def MenuUrut(Menu2):
    os.system('cls')
    print("<<MENU PILIHAN>>")
    print("1. Nama")
    print("2. Jeni Kelami")
    print("3. Keluhan")
    print("4. Tekanan Darah")
    print("5. Denyut Nadi")
    print("6. Suhu")
    print("7. Saturasi Oksigen")
    print("8. Tanggal")
    print("9. Bulan")
    
    print("0. Keluar")
    Menu2 = int(input("Pilihan Anda? "))
    return Menu2
 
#subrutin mengisi data rekam medis   
def IsiLarik(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    print("<<PENGISIAN DATA REKAM MEDIS>>")
    print("------------------------------")
    N = int(input("Banyak data yang akan diisi : "))
    if (N < MAKSDATA):
        for i in range(N):
            print(f"Data Rekam Medis ke-{i+1}")
            Nama[i] = str(input("Nama Pasien           : ")).upper()
            JK[i] = str(input("Jenis Kelamin         : ")).upper()
            Keluhan[i] = str(input("Keluhan Pasien        : ")).upper()
            TD[i] = str(input("Tekanan Darah (../..) : ")).upper()
            DN[i] = str(input("Denyut Nadi           : ")).upper()
            Suhu[i] = str(input("Suhu                  : ")).upper()
            SO[i] = str(input("Saturasi Oksigen (%)  : ")).upper()
            Tanggal[i] = str(input("Tanggal               : ")).upper()
            Bulan[i] = str(input("Bulan                 : ")).upper()
            Tahun[i] = str(input("Tahun                 : ")).upper()
        return N

#subrutin menambah data rekam medis
def TambahData(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    print("<<PENAMMBAHAN DATA REKAM MEDIS>>")
    print("--------------------------------")
    if (N < MAKSDATA):
        print(f"Data Rekam Medis ke-{N}")
        Nama[N] = str(input("Nama Pasien           : ")).upper()
        JK[N] = str(input("Jenis Kelamin         : ")).upper()
        Keluhan[N] = str(input("Keluhan Pasien        : ")).upper()
        TD[N] = str(input("Tekanan Darah (../..) : ")).upper()
        DN[N] = str(input("Denyut Nadi           : ")).upper()
        Suhu[N] = str(input("Suhu                  : ")).upper()
        SO[N] = str(input("Saturasi Oksigen (%)  : ")).upper()
        Tanggal[N] = str(input("Tanggal               : ")).upper()
        Bulan[N] = str(input("Bulan                 : ")).upper()
        Tahun[N] = str(input("Tahun                 : ")).upper()
        N = N + 1
        return N
    else:
        "Isi Data Rekam Medis Terlebih Dahulu"
    
#subrutin hapus data rekam medis
def HapusData(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    print("<<PENGHAPUSAN DATA REKAM MEDIS>>")
    print("--------------------------------")
    PosisiHapus = int(input("Nomor Data yang Akan Dihapus : "))
    if (N > 0):
        if (PosisiHapus-1 >= 1) and (PosisiHapus-1 <= N):
            for i in range(PosisiHapus, N, 1):
                Nama[i-1] = Nama[i]
                JK[i-1] = JK[i]
                Keluhan[i-1] = Keluhan[i]
                TD[i-1] = TD[i]
                DN[i-1] = DN[i]
                Suhu[i-1] = Suhu[i]
                SO[i-1] = SO[i]
                Tanggal[i-1] = Tanggal[i]
                Bulan[i-1] = Bulan[i]
                Tahun[i-1] = Tahun[i]
            Nama[N-1] = 0
            N = N - 1
            return N
        else:
            print("Posisi Tidak Valid")
    else:
        print("Data Kosong")
                
#subrutin metode urut bubble sort ascending
def BubbleAscNama(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-1, i-1, -1):
            if (Nama[j] < Nama[j-1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp
                
                #Tukar JK
                Temp = JK[j]
                JK[j] = JK[j-1]
                JK[j-1] = Temp
                
                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j-1]
                Keluhan[j-1] = Temp
                
                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j-1]
                TD[j-1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j-1]
                DN[j-1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j-1]
                Suhu[j-1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j-1]
                SO[j-1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j-1]
                Bulan[j-1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j-1]
                Tahun[j-1] = Temp
                
def BubbleAscKeluhan(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-1, i-1, -1):
            if (Keluhan[j] < Keluhan[j-1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp
                
                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j-1]
                Keluhan[j-1] = Temp
                
                #Tukar JK
                Temp = JK[j]
                JK[j] = JK[j-1]
                JK[j-1] = Temp

                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j-1]
                TD[j-1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j-1]
                DN[j-1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j-1]
                Suhu[j-1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j-1]
                SO[j-1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j-1]
                Bulan[j-1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j-1]
                Tahun[j-1] = Temp

def BubbleAscTD(N, Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-1, i-1, -1):
            if (TD[j] < TD[j-1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp
                
                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j-1]
                Keluhan[j-1] = Temp
                
                #Tukar JK
                Temp = JK[j]
                JK[j] = JK[j-1]
                JK[j-1] = Temp

                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j-1]
                TD[j-1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j-1]
                DN[j-1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j-1]
                Suhu[j-1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j-1]
                SO[j-1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j-1]
                Bulan[j-1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j-1]
                Tahun[j-1] = Temp
                
def BubbleAscDN(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-1, i-1, -1):
            if (DN[j] < DN[j-1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp
                
                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j-1]
                Keluhan[j-1] = Temp
                
                #Tukar JK
                Temp = JK[j]
                JK[j] = JK[j-1]
                JK[j-1] = Temp

                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j-1]
                TD[j-1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j-1]
                DN[j-1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j-1]
                Suhu[j-1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j-1]
                SO[j-1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j-1]
                Bulan[j-1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j-1]
                Tahun[j-1] = Temp
                
def BubbleAscSuhu(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-1, i-1, -1):
            if (Suhu[j] < Suhu[j-1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp
                
                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j-1]
                Keluhan[j-1] = Temp
                
                #Tukar JK
                Temp = JK[j]
                JK[j] = JK[j-1]
                JK[j-1] = Temp

                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j-1]
                TD[j-1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j-1]
                DN[j-1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j-1]
                Suhu[j-1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j-1]
                SO[j-1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j-1]
                Bulan[j-1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j-1]
                Tahun[j-1] = Temp

def BubbleAscSO(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-1, i-1, -1):
            if (SO[j] < SO[j-1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp
                
                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j-1]
                Keluhan[j-1] = Temp
                
                #Tukar JK
                Temp = JK[j]
                JK[j] = JK[j-1]
                JK[j-1] = Temp

                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j-1]
                TD[j-1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j-1]
                DN[j-1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j-1]
                Suhu[j-1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j-1]
                SO[j-1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j-1]
                Bulan[j-1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j-1]
                Tahun[j-1] = Temp

def BubbleAscTanggal(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-1, i-1, -1):
            if (Tanggal[j] < Tanggal[j-1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp
                
                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j-1]
                Keluhan[j-1] = Temp
                
                #Tukar JK
                Temp = JK[j]
                JK[j] = JK[j-1]
                JK[j-1] = Temp

                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j-1]
                TD[j-1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j-1]
                DN[j-1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j-1]
                Suhu[j-1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j-1]
                SO[j-1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j-1]
                Bulan[j-1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j-1]
                Tahun[j-1] = Temp

def BubbleAscBulan(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-1, i-1, -1):
            if (Bulan[j] < Bulan[j-1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp
                
                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j-1]
                Keluhan[j-1] = Temp
                
                #Tukar JK
                Temp = JK[j]
                JK[j] = JK[j-1]
                JK[j-1] = Temp

                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j-1]
                TD[j-1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j-1]
                DN[j-1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j-1]
                Suhu[j-1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j-1]
                SO[j-1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j-1]
                Bulan[j-1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j-1]
                Tahun[j-1] = Temp

def BubbleAscTahun(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-1, i-1, -1):
            if (Tahun[j] < Tahun[j-1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp
                
                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j-1]
                Keluhan[j-1] = Temp
                
                #Tukar JK
                Temp = JK[j]
                JK[j] = JK[j-1]
                JK[j-1] = Temp

                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j-1]
                TD[j-1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j-1]
                DN[j-1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j-1]
                Suhu[j-1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j-1]
                SO[j-1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j-1]
                Bulan[j-1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j-1]
                Tahun[j-1] = Temp

#subrutin metode urut bubble sort decending
def BubbleDscNama(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-i):
            if (Nama[j] < Nama[j+1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j+1] = Temp
                
                # Tukar JK
                Temp = JK[j]
                JK[j] = JK[j+1]
                JK[j+1] = Temp
                
                # Tukar JK
                Temp = JK[j]
                JK[j] = JK[j+1]
                JK[j+1] = Temp

                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j+1]
                Keluhan[j+1] = Temp
                
                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j+1]
                TD[j+1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j+1]
                DN[j+1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j+1]
                Suhu[j+1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j+1]
                SO[j+1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j+1]
                Bulan[j+1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp

def BubbleDscKeluhan(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-i):
            if (Keluhan[j] < Keluhan[j+1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j+1] = Temp
                
                # Tukar JK
                Temp = JK[j]
                JK[j] = JK[j+1]
                JK[j+1] = Temp

                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j+1]
                Keluhan[j+1] = Temp
                
                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j+1]
                TD[j+1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j+1]
                DN[j+1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j+1]
                Suhu[j+1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j+1]
                SO[j+1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j+1]
                Bulan[j+1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp

def BubbleDscTD(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-i):
            if (TD[j] < TD[j+1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j+1] = Temp
                
                # Tukar JK
                Temp = JK[j]
                JK[j] = JK[j+1]
                JK[j+1] = Temp

                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j+1]
                Keluhan[j+1] = Temp
                
                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j+1]
                TD[j+1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j+1]
                DN[j+1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j+1]
                Suhu[j+1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j+1]
                SO[j+1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j+1]
                Bulan[j+1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp

def BubbleDscDN(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-i):
            if (DN[j] < DN[j+1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j+1] = Temp
                
                # Tukar JK
                Temp = JK[j]
                JK[j] = JK[j+1]
                JK[j+1] = Temp

                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j+1]
                Keluhan[j+1] = Temp
                
                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j+1]
                TD[j+1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j+1]
                DN[j+1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j+1]
                Suhu[j+1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j+1]
                SO[j+1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j+1]
                Bulan[j+1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp

def BubbleDscSuhu(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-i):
            if (Suhu[j] < Suhu[j+1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j+1] = Temp
                
                # Tukar JK
                Temp = JK[j]
                JK[j] = JK[j+1]
                JK[j+1] = Temp

                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j+1]
                Keluhan[j+1] = Temp
                
                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j+1]
                TD[j+1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j+1]
                DN[j+1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j+1]
                Suhu[j+1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j+1]
                SO[j+1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j+1]
                Bulan[j+1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp

def BubbleDscSO(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-i):
            if (SO[j] < SO[j+1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j+1] = Temp
                
                # Tukar JK
                Temp = JK[j]
                JK[j] = JK[j+1]
                JK[j+1] = Temp

                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j+1]
                Keluhan[j+1] = Temp
                
                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j+1]
                TD[j+1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j+1]
                DN[j+1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j+1]
                Suhu[j+1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j+1]
                SO[j+1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j+1]
                Bulan[j+1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp

def BubbleDscTanggal(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-i):
            if (Tanggal[j] < Tanggal[j+1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j+1] = Temp
                
                # Tukar JK
                Temp = JK[j]
                JK[j] = JK[j+1]
                JK[j+1] = Temp

                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j+1]
                Keluhan[j+1] = Temp
                
                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j+1]
                TD[j+1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j+1]
                DN[j+1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j+1]
                Suhu[j+1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j+1]
                SO[j+1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j+1]
                Bulan[j+1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp

def BubbleDscBulan(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-i):
            if (Bulan[j] < Bulan[j+1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j+1] = Temp
                
                # Tukar JK
                Temp = JK[j]
                JK[j] = JK[j+1]
                JK[j+1] = Temp

                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j+1]
                Keluhan[j+1] = Temp
                
                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j+1]
                TD[j+1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j+1]
                DN[j+1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j+1]
                Suhu[j+1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j+1]
                SO[j+1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j+1]
                Bulan[j+1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp

def BubbleDscTahun(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    os.system('cls')
    for i in range(1, N):
        for j in range(N-i):
            if (Tahun[j] < Tahun[j+1]):
                # Tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j+1] = Temp
                
                # Tukar JK
                Temp = JK[j]
                JK[j] = JK[j+1]
                JK[j+1] = Temp

                #Tukar Keluhan
                Temp = Keluhan[j]
                Keluhan[j] = Keluhan[j+1]
                Keluhan[j+1] = Temp
                
                #Tukar TD
                Temp = TD[j]
                TD[j] = TD[j+1]
                TD[j+1] = Temp
                
                #Tukar DN
                Temp = DN[j]
                DN[j] = DN[j+1]
                DN[j+1] = Temp
                
                #Tukar Suhu
                Temp = Suhu[j]
                Suhu[j] = Suhu[j+1]
                Suhu[j+1] = Temp
                
                #Tukar SO
                Temp = SO[j]
                SO[j] = SO[j+1]
                SO[j+1] = Temp
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp
                
                #Tukar Bulan
                Temp = Bulan[j]
                Bulan[j] = Bulan[j+1]
                Bulan[j+1] = Temp
                
                #Tukar Tahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp

#subrutin metode urut maximum sort ascending
def MaxAscNama(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = 0
        for j in range(1,N+1-i):
            if (Nama[j] > Nama[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp
        
def MaxAscJK(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = 0
        for j in range(1,N+1-i):
            if (JK[j] > JK[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp
        
def MaxAscKeluhan(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = 0
        for j in range(1,N+1-i):
            if (Keluhan[j] > Keluhan[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxAscTD(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = 0
        for j in range(1,N+1-i):
            if (Keluhan[j] > Keluhan[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxAscDN(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = 0
        for j in range(1,N+1-i):
            if (DN[j] > DN[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxAscSuhu(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = 0
        for j in range(1,N+1-i):
            if (Suhu[j] > Suhu[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxAscSO(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = 0
        for j in range(1,N+1-i):
            if (SO[j] > SO[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxAscTanggal(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = 0
        for j in range(1,N+1-i):
            if (Tanggal[j] > Tanggal[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxAscBulan(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = 0
        for j in range(1,N+1-i):
            if (Bulan[j] > Bulan[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxAscTahun(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = 0
        for j in range(1,N+1-i):
            if (Tahun[j] > Tahun[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

#subrutin metode urut maximum sort decending
def MaxDscNama(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = i
        for j in range(1,N+1-i):
            if (Nama[j] > Nama[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp


        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxDscJK(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = i
        for j in range(1,N+1-i):
            if (JK[j] > JK[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxDscKeluhan(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = i
        for j in range(1,N+1-i):
            if (Keluhan[j] > Keluhan[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxDscTD(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = i
        for j in range(1,N+1-i):
            if (TD[j] > TD[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxDscDN(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = i
        for j in range(1,N+1-i):
            if (DN[j] > DN[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxDscSuhu(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = i
        for j in range(1,N+1-i):
            if (Suhu[j] > Suhu[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxDscSO(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = i
        for j in range(1,N+1-i):
            if (SO[j] > SO[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxDscTanggal(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = i
        for j in range(1,N+1-i):
            if (Tanggal[j] > Tanggal[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
       
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[max]
        JK[max] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxDscBulan(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = i
        for j in range(1,N+1-i):
            if (Bulan[j] > Bulan[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp

def MaxDscTahun(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        max = i
        for j in range(1,N+1-i):
            if (Tahun[j] > Tahun[max]):
                max = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[max]
        Keluhan[max] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[max]
        TD[max] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[max]
        DN[max] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[max]
        Suhu[max] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[max]
        SO[max] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[max]
        Bulan[max] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[max]
        Tahun[max] = Temp
#subrutin metode urut minimum sort ascending
def MinAscNama(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (Nama[j] < Nama[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp    

def MinAscJK(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (JK[j] < JK[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp    

def MinAscKeluhan(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (Keluhan[j] < Keluhan[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp    

def MinAscTD(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (TD[j] < TD[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp    

def MinAscDN(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (DN[j] < DN[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp    

def MinAscSuhu(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (Suhu[j] < Suhu[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp    

def MinAscSO(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (SO[j] < SO[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp    

def MinAscTanggal(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (Tanggal[j] < Tanggal[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp    

def MinAscBulan(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (Bulan[j] < Bula[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp    

def MinAscTahun(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (Tahun[j] < Tahun[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp    

#subrutin metode urut minimum sort decending
def MinDscNama(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (Nama[j] < Nama[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp

def MinDscJK(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (J[j] < J[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp

def MinDscKeluhan(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (Keluhan[j] < Keluhan[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp

def MinDscTD(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (TD[j] < TD[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp

def MinDscDN(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (DN[j] < DN[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp

def MinDscSuhu(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (Suhu[j] < Suhu[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp

def MinDscSO(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (SO[j] < SO[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp

def MinDscTanggal(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (Tanggal[j] < Tanggal[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp

def MinDscBulan(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (Bulan[j] < Bulan[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp

def MinDscTahun(N ,Nama, JK, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (Tahun[j] < Tahun[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar DN
        Temp = DN[j]
        DN[j] = DN[min]
        DN[min] = Temp
        
        #Tukar Suhu
        Temp = Suhu[j]
        Suhu[j] = Suhu[min]
        Suhu[min] = Temp
        
        #Tukar SO
        Temp = SO[j]
        SO[j] = SO[min]
        SO[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp
        
        #Tukar Bulan
        Temp = Bulan[j]
        Bulan[j] = Bulan[min]
        Bulan[min] = Temp
        
        #Tukar Tahun
        Temp = Tahun[j]
        Tahun[j] = Tahun[min]
        Tahun[min] = Temp


#Badan Program
#Penciptaan larik nama, jenis kelamin (JK), keluhan, Tekanan Darah (TD), Denyut Nadi (DN), Suhu,
#Saturasi Oksigen (SO), Tanggal, Bulan, Tahun
Nama = ['/'] * MAKSDATA
JK = ['/'] * MAKSDATA
Keluhan = ['/'] * MAKSDATA
TD = ['/'] * MAKSDATA
DN = ['/'] * MAKSDATA
Suhu = ['/'] * MAKSDATA
SO = ['/'] * MAKSDATA
Tanggal = ['/'] * MAKSDATA
Bulan = ['/'] * MAKSDATA
Tahun = ['/'] * MAKSDATA

os.system('cls')
Menu = 0
Menu = MenuPilihan(Menu)
N = 0
while (Menu != 0):
    os.system('cls')
    match (Menu):
        case 1: #Isi Data
            N = IsiLarik(N ,Nama, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun)
        case 2: #Tampil Data
            if (N > 0):
                TampilRekamMedis(N ,Nama, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun)
            else:
                print("Isi Data Rekam Medis Terlebih Dahulu")
            print()
            os.system('pause')
        case 3: #Tambah Data
            N = TambahData(N ,Nama, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun)
        case 4: #Hapus Data
            N = HapusData(N ,Nama, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun)
        case 5: #Urut Data
            BubbleAscNama(N ,Nama, Keluhan, TD, DN, Suhu, SO, Tanggal, Bulan, Tahun)
            
    os.system('cls')
    Menu = MenuPilihan(Menu)