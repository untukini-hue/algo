#Program Rekam Medis
#I.S :
#F.S :
import os

#KONSTANTA
MAKSDATA = 30

#subrutin menampilkan data Rekam Medis dalam bentuk tabel
def TampilRekamMedis(N ,Nama, JK, Keluhan, TD, Tanggal):
    os.system('cls')
    print('                                                 DAFTAR REKAM MEDIS')
    print('                                                 ------------------')
    print('----------------------------------------------------------------------------------------------')
    print('|  No  |      Nama Pasien      | Jenis Kelamin |     Keluhan     | Tekanan Darah |  Tanggal  |')
    print('-----------------------------------------------------------------------------------------------')
    for i in range(N):
        print(f'| {i+1:>4} | {Nama[i]:>21} | {JK[i]:>13} | {Keluhan[i]:>15} | {TD[i]:^13} | {Tanggal[i]:^10} |')
    print('-----------------------------------------------------------------------------------------------------')
    
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

#subrutin menu untuk memilih apa yang akan diurutkan
def MenuUrut(Menu2):
    os.system('cls')
    print("<<MENU>>")
    print("1. Nama")
    print("2. Jenis Kelamin")
    print("3. Keluhan")
    print("4. Tekanan Darah")
    print("5. Tanggal")
    print("0. Keluar")
    Menu2 = int(input("Apa yang akan diurutkan? "))
    return Menu2
 
#subrutin menu untuk memilih metode urut
def MenuMetode(Menu3):
    print("<<MENU METODE URUT>>")
    print("1. Bubble Sort Ascending")
    print("2. Bubble Sort Decending")
    print("3. Maximum Sort Ascending")
    print("4. Maximum Sort Decending")
    print("5. Minimum Sort Ascending")
    print("6. Minimum Sort Decending")
    print("0. Keluar")
    Menu3 = int(input("Menggunakan Metode Apa? "))
    return Menu3

#subrutin mengisi data rekam medis   
def IsiLarik(N ,Nama, JK, Keluhan, TD, Tanggal):
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
            Tanggal[i] = str(input("Tanggal               : ")).upper()
        return N

#subrutin menambah data rekam medis
def TambahData(N ,Nama, JK, Keluhan, TD, Tanggal):
    os.system('cls')
    print("<<PENAMMBAHAN DATA REKAM MEDIS>>")
    print("--------------------------------")
    if (N < MAKSDATA):
        print(f"Data Rekam Medis ke-{N}")
        Nama[N] = str(input("Nama Pasien           : ")).upper()
        JK[N] = str(input("Jenis Kelamin         : ")).upper()
        Keluhan[N] = str(input("Keluhan Pasien        : ")).upper()
        TD[N] = str(input("Tekanan Darah (../..) : ")).upper()
        Tanggal[N] = str(input("Tanggal               : ")).upper()
        N = N + 1
        return N
    else:
        "Isi Data Rekam Medis Terlebih Dahulu"
    
#subrutin hapus data rekam medis
def HapusData(N ,Nama, JK, Keluhan, TD, Tanggal):
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
                Tanggal[i-1] = Tanggal[i]
            Nama[N-1] = 0
            N = N - 1
            return N
        else:
            print("Posisi Tidak Valid")
    else:
        print("Data Kosong")
                
#subrutin metode urut bubble sort ascending
def BubbleAscNama(N ,Nama, JK, Keluhan, TD, Tanggal):
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
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp
 
def BubbleAscJK(N ,Nama, JK, Keluhan, TD, Tanggal):
    for i in range(1, N):
        for j in range(N-1, i-1, -1):
            if (JK[j] < JK[j-1]):
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
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp
               
def BubbleAscKeluhan(N ,Nama, JK, Keluhan, TD, Tanggal):
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
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp

def BubbleAscTD(N, Nama, JK, Keluhan, TD, Tanggal):
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
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp        
                
def BubbleAscTanggal(N ,Nama, JK, Keluhan, TD, Tanggal):

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
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j-1]
                Tanggal[j-1] = Temp

#subrutin metode urut bubble sort decending
def BubbleDscNama(N ,Nama, JK, Keluhan, TD, Tanggal):

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
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp

def BubbleDscJK(N ,Nama, JK, Keluhan, TD, Tanggal):

    for i in range(1, N):
        for j in range(N-i):
            if (JK[j] < JK[j+1]):
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
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp

def BubbleDscKeluhan(N ,Nama, JK, Keluhan, TD, Tanggal):

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
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp

def BubbleDscTD(N ,Nama, JK, Keluhan, TD, Tanggal):

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
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp



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
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp

def BubbleDscTanggal(N ,Nama, JK, Keluhan, TD, Tanggal):

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
                
                #Tukar Tanggal
                Temp = Tanggal[j]
                Tanggal[j] = Tanggal[j+1]
                Tanggal[j+1] = Temp

#subrutin metode urut maximum sort ascending
def MaxAscNama(N ,Nama, JK, Keluhan, TD, Tanggal):
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
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
def MaxAscJK(N ,Nama, JK, Keluhan, TD, Tanggal):
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
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp
        
def MaxAscKeluhan(N ,Nama, JK, Keluhan, TD, Tanggal):
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
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp

def MaxAscTD(N ,Nama, JK, Keluhan, TD, Tanggal):
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
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp

def MaxAscTanggal(N ,Nama, JK, Keluhan, TD, Tanggal):
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
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp

#subrutin metode urut maximum sort decending
def MaxDscNama(N ,Nama, JK, Keluhan, TD, Tanggal):
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
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp

def MaxDscJK(N ,Nama, JK, Keluhan, TD, Tanggal):
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
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp

def MaxDscKeluhan(N ,Nama, JK, Keluhan, TD, Tanggal):
    for i in range(1,N):
        max = i
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
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp

def MaxDscTD(N ,Nama, JK, Keluhan, TD, Tanggal):
    for i in range(1,N):
        max = i
        for j in range(1,N+1-i):
            if (TD[j] > TD[max]):
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
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp

def MaxDscTanggal(N ,Nama, JK, Keluhan, TD, Tanggal):
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
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[max]
        Tanggal[max] = Temp

#subrutin metode urut minimum sort ascending
def MinAscNama(N ,Nama, JK, Keluhan, TD, Tanggal):
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
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp    

def MinAscJK(N ,Nama, JK, Keluhan, TD, Tanggal):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (JK[j] < JK[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[min]
        JK[min] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp    

def MinAscKeluhan(N ,Nama, JK, Keluhan, TD, Tanggal):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (Keluhan[j] < Keluhan[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[min]
        JK[min] = Temp        
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp    

def MinAscTD(N ,Nama, JK, Keluhan, TD, Tanggal):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (TD[j] < TD[min]):
                min = j
        
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
       
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[min]
        JK[min] = Temp

        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp    

def MinAscTanggal(N ,Nama, JK, Keluhan, TD, Tanggal):
    for i in range(1,N):
        min = i
        for j in range(1,N+1-i):
            if (Tanggal[j] < Tanggal[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[min]
        JK[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp    

#subrutin metode urut minimum sort decending
def MinDscNama(N ,Nama, JK, Keluhan, TD, Tanggal):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (Nama[j] < Nama[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[min]
        JK[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp

def MinDscJK(N ,Nama, JK, Keluhan, TD, Tanggal):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (J[j] < J[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[min]
        JK[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp

def MinDscKeluhan(N ,Nama, JK, Keluhan, TD, Tanggal):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (Keluhan[j] < Keluhan[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
         # Tukar JK
        Temp = JK[j]
        JK[j] = JK[min]
        JK[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp

def MinDscTD(N ,Nama, JK, Keluhan, TD, Tanggal):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (TD[j] < TD[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[min]
        JK[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp

def MinDscTanggal(N ,Nama, JK, Keluhan, TD, Tanggal):
    for i in range(1,N):
        min = 0
        for j in range(1,N+1-i):
            if (Tanggal[j] < Tanggal[min]):
                min = j
                
        # Tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp
        
        # Tukar JK
        Temp = JK[j]
        JK[j] = JK[min]
        JK[min] = Temp
        
        #Tukar Keluhan
        Temp = Keluhan[j]
        Keluhan[j] = Keluhan[min]
        Keluhan[min] = Temp
        
        #Tukar TD
        Temp = TD[j]
        TD[j] = TD[min]
        TD[min] = Temp
        
        #Tukar Tanggal
        Temp = Tanggal[j]
        Tanggal[j] = Tanggal[min]
        Tanggal[min] = Temp

#Badan Program
#Penciptaan larik nama, jenis kelamin (JK), keluhan, Tekanan Darah (TD), Denyut Nadi (DN), Suhu,
#Saturasi Oksigen (SO), Tanggal, Bulan, Tahun
Nama = ['/'] * MAKSDATA
JK = ['/'] * MAKSDATA
Keluhan = ['/'] * MAKSDATA
TD = ['/'] * MAKSDATA
Tanggal = ['/'] * MAKSDATA

os.system('cls')
Menu = 0
Menu = MenuPilihan(Menu)
N = 0
while (Menu != 0):
    os.system('cls')
    match (Menu):
        case 1: #Isi Data
            N = IsiLarik(N ,Nama, JK, Keluhan, TD, Tanggal)
        case 2: #Tampil Data
            if (N > 0):
                TampilRekamMedis(N ,Nama, JK, Keluhan, TD, Tanggal)
            else:
                print("Isi Data Rekam Medis Terlebih Dahulu")
            print()
            os.system('pause')
        case 3: #Tambah Data
            N = TambahData(N ,Nama, JK, Keluhan, TD, Tanggal)
        case 4: #Hapus Data
            N = HapusData(N ,Nama, JK, Keluhan, TD, Tanggal)
        case 5: #Urut Data
            Menu2 = 0
            Menu2 = MenuUrut(Menu2)
            while (Menu2 != 0):
                match (Menu2):
                    case 1: # Urut Nama
                        Menu3 = 0
                        Menu3 = MenuMetode(Menu3)
                        while (Menu3 != 0):
                            match (Menu3):
                                case 1: #Bubble Sort Ascending
                                    BubbleAscNama(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 2: #Bubble Sort Decending
                                    BubbleDscNama(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 3: #Maximum Sort Ascending
                                    MaxAscNama(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 4: #Maximum Sort Decending
                                    MaxDscNama(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 5: #Minimum Sort Ascending
                                    MinAscNama(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 6: #Minimum Sort Decending
                                    MinDscNama(N ,Nama, JK, Keluhan, TD, Tanggal)
                    case 2: #urut Jenis Kelamin
                        Menu3 = 0
                        Menu3 = MenuMetode(Menu3)
                        while (Menu3 != 0):
                            match (Menu3):
                                case 1: #Bubble Sort Ascending
                                    BubbleAscJK(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 2: #Bubble Sort Decending
                                    BubbleDscJK(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 3: #Maximum Sort Ascending
                                    MaxAscJK(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 4: #Maximum Sort Decending
                                    MaxDscJK(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 5: #Minimum Sort Ascending
                                    MinAscJK(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 6: #Minimum Sort Decending
                                    MinDscJK(N ,Nama, JK, Keluhan, TD, Tanggal)
                    case 3: #urut Keluhan
                        Menu3 = 0
                        Menu3 = MenuMetode(Menu3)
                        while (Menu3 != 0):
                            match (Menu3):
                                case 1: #Bubble Sort Ascending
                                    BubbleAscKeluhan(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 2: #Bubble Sort Decending
                                    BubbleDscKeluhan(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 3: #Maximum Sort Ascending
                                    MaxAscKeluhan(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 4: #Maximum Sort Decending
                                    MaxDscKeluhan(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 5: #Minimum Sort Ascending
                                    MinAscKeluhan(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 6: #Minimum Sort Decending
                                    MinDscKeluhan(N ,Nama, JK, Keluhan, TD, Tanggal)
                    case 4: #urut TD
                        Menu3 = 0
                        Menu3 = MenuMetode(Menu3)
                        while (Menu3 != 0):
                            match (Menu3):
                                case 1: #Bubble Sort Ascending
                                    BubbleAscTD(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 2: #Bubble Sort Decending
                                    BubbleDscTD(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 3: #Maximum Sort Ascending
                                    MaxAscTD(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 4: #Maximum Sort Decending
                                    MaxDscTD(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 5: #Minimum Sort Ascending
                                    MinAscTD(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 6: #Minimum Sort Decending
                                    MinDscTD(N ,Nama, JK, Keluhan, TD, Tanggal)
                    case 5: #urut Tanggal
                        Menu3 = 0
                        Menu3 = MenuMetode(Menu3)
                        while (Menu3 != 0):
                            match (Menu3):
                                case 1: #Bubble Sort Ascending
                                    BubbleAscTanggal(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 2: #Bubble Sort Decending
                                    BubbleDscTanggal(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 3: #Maximum Sort Ascending
                                    MaxAscTanggal(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 4: #Maximum Sort Decending
                                    MaxDscTanggal(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 5: #Minimum Sort Ascending
                                    MinAscTanggal(N ,Nama, JK, Keluhan, TD, Tanggal)
                                case 6: #Minimum Sort Decending
                                    MinDscTanggal(N ,Nama, JK, Keluhan, TD, Tanggal)
                                        
    
    
    os.system('cls')
    Menu = MenuPilihan(Menu)   