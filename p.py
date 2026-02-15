#Program Pengolahan Larik Buku
#I.S.: pengguna memasukkan bulan, tahun dan data buku
#F.S.: meanmpilkan daftar buku dalam bentuk tabel
import os

#konstanta
MAKSBUKU = 30

#subrutin menu pilihan
def MenuPilihan(Menu):
    os.system('cls')
    print('<< MENU PILIHAN >>')
    print('1. Isi Data Buku')
    print('2. Tampil Data Buku')
    print('3. Urut Data Buku')
    print('4. Cari Data Buku')
    print('0. Keluar')
    Menu = int(input('Pilihan Anda? '))
    return Menu

#subrutin menu pengurutan
def MenuPengurutan(Menu2,Keterngan):
    os.system('cls')
    print(f'<< MENU {Keterangan} >>')
    print('1. Kode Buku')
    print('2. Nama Buku')
    print('3. Jenis Buku')
    print('4. Stok Buku')
    print('0. Kembali Ke Menu Pilihan')
    Menu2 = int(input('Pilihan Anda? '))
    return Menu2

#subrutin menentukan jenis buku
def JenisBuku(Kode):
    if (Kode[0:3] == '000'):
        return 'Karya Umum'
    elif (Kode[0:3] == '100'):
        return 'Filsafat & Psikologi'
    elif (Kode[0:3] == '200'):
        return 'Agama'
    elif (Kode[0:3] == '300'):
        return 'Ilmu Politik & Ekonomi'
    elif (Kode[0:3] == '400'):
        return 'Bahasa'
    elif (Kode[0:3] == '500'):
        return 'Ilmu Pengetahuan Alam & Matematik'
    elif (Kode[0:3] == '600'):
        return 'Teknologi & Ilmu Terapan'
    elif (Kode[0:3] == '700'):
        return 'Seni, Hiburan & Olahraga'
    elif (Kode[0:3] == '800'):
        return 'Kesusastraan'
    else:
        return 'Sejarah & Geografi'

#subrutin memasukkan data buku
def IsiData(KB,NB,JB,Stok,N):
    os.system('cls')
    print('PENGISIAN DATA BUKU')
    print('===================')
    i = 0
    print(f'Data Buku Ke-{i+1}')
    KB[i] = str(input('Kode Buku  : ')).upper()
    while (KB[i] != 'STOP'):
        NB[i] = str(input('Nama Buku  : ')).upper()
        JB[i] = JenisBuku(KB[i])
        print(f'Jenis Buku : {JB[i]}')
        Stok[i] = int(input('Stok Buku  : '))

        #memasukkan data buku selanjutnya
        print()
        i += 1
        print(f'Data Buku Ke-{i+1}')
        KB[i] = str(input('Kode Buku  : ')).upper()

    N = i
    return N

#subrutin menampilkan daftar buku dalam bentuk tabel
def TampilBuku(Bulan,Tahun,N,KB,NB,JB,Stok):
    os.system('cls')
    print('                                     DAFTAR BUKU')
    print('                                     -----------')
    print(f'Bulan : {Bulan}')
    print(f'Tahun : {Tahun}')
    print('------------------------------------------------------------------------------------')
    print('| No | Kode Buku |      Nama Buku      |             Jenis Buku             | Stok |')
    print('------------------------------------------------------------------------------------')
    for i in range(N):
        print(f'| {i+1:>2} | {KB[i]:>9} | {NB[i]:>19} | {JB[i]:>34} | {Stok[i]:4} |')

    print('------------------------------------------------------------------------------------')

#subrutin mengurutkan kode buku secara ascending menggunakan Bubble Sort
def UrutKodeAsc(KB,NB,JB,Stok,N):
    for i in range(1,N):
        for j in range(N-1,i-1,-1):
            if (KB[j] < KB[j-1]):
                #tukar kode buku
                Temp = KB[j]
                KB[j] = KB[j-1]
                KB[j-1] = Temp

                #tukar nama buku
                Temp = NB[j]
                NB[j] = NB[j-1]
                NB[j-1] = Temp

                #tukar jenis buku
                Temp = JB[j]
                JB[j] = JB[j-1]
                JB[j-1] = Temp

                #tukar stok buku
                Temp = Stok[j]
                Stok[j] = Stok[j-1]
                Stok[j-1] = Temp

#subrutin mengurutkan nama buku secara descending menggunakan Bubble Sort
def UrutNamaDsc(KB,NB,JB,Stok,N):
    for i in range(1,N):
        for j in range(N-i):
            if (NB[j] < NB[j+1]):
                #tukar kode buku
                Temp = KB[j]
                KB[j] = KB[j+1]
                KB[j+1] = Temp

                #tukar nama buku
                Temp = NB[j]
                NB[j] = NB[j+1]
                NB[j+1] = Temp

                #tukar jenis buku
                Temp = JB[j]
                JB[j] = JB[j+1]
                JB[j+1] = Temp

                #tukar stok buku
                Temp = Stok[j]
                Stok[j] = Stok[j+1]
                Stok[j+1] = Temp

#subrutin mengurutkan jenis buku secara ascending menggunakan Maximum Sort
def UrutJenisAsc(KB,NB,JB,Stok,N):
    for i in range(1,N):
        max = 0
        for j in range(1,N+1-i):
            if (JB[j] > JB[max]):
                max = j

        #tukar kode buku
        Temp = KB[max]
        KB[max] = KB[j]
        KB[j] = Temp

        #tukar nama buku
        Temp = NB[max]
        NB[max] = NB[j]
        NB[j] = Temp

        #tukar jenis buku
        Temp = JB[max]
        JB[max] = JB[j]
        JB[j] = Temp

        #tukar stok buku
        Temp = Stok[max]
        Stok[max] = Stok[j]
        Stok[j] = Temp

#subrutin mengurutkan jenis buku secara descending menggunakan Maximum Sort
def UrutStokDsc(KB,NB,JB,Stok,N):
    for i in range(1,N):
        max = i
        for j in range(i+1,N):
            if (Stok[j] > Stok[max]):
                max = j

        #tukar kode buku
        Temp = KB[max]
        KB[max] = KB[i]
        KB[i] = Temp

        #tukar nama buku
        Temp = NB[max]
        NB[max] = NB[i]
        NB[i] = Temp

        #tukar jenis buku
        Temp = JB[max]
        JB[max] = JB[i]
        JB[i] = Temp

        #tukar stok buku
        Temp = Stok[max]
        Stok[max] = Stok[i]
        Stok[i] = Temp

#subrutin mencari kode buku menggunakan binary search pada data terurut ascending
def CariKodeAsc(KB2,NB2,JB2,Stok2,N):
    #memasukkan kode buku yang dicari
    KodeCari = str(input('Kode Buku yang dicari : ')).upper()
    #proses pencarian
    Ia = 0
    Ib = N-1
    Ketemu = False
    while (not Ketemu) and (Ia <= Ib):
        k = (Ia + Ib) // 2
        if (KB2[k] == KodeCari):
            Ketemu = True
        else:
            if (KB2[k] < KodeCari):
                #pencarian dilanjutkan kebagian kanan
                Ia = k + 1
            else:
                #pencarian dilanjutkan kebagian kiri
                Ib = k - 1

    if (Ketemu):
        os.system('cls')
        print(f'<< PENCARIAN KODE BUKU {KodeCari} >>')
        print(f'Nama Buku  : {NB2[k]}')
        print(f'Jenis Buku : {JB2[k]}')
        print(f'Stok Buku  : {Stok2[k]}')
    else:
        print(f'Kode buku {KodeCari} tidak ditemukan!')

#subrutin mencari jenis buku menggunakan sequential search dengan sentinel
def CariJenis(KB,NB,JB,Stok,N):
    #memasukkan kode buku yang dicari
    JenisCari = str(input('Jenis Buku yang dicari : '))
    #proses pencarian
    i = 0
    JB[N] = JenisCari
    while (JB[i] != JenisCari):
        i += 1

    if (i < N):
        os.system('cls')
        print(f'   << PENCARIAN JENIS BUKU "{JenisCari}" >>')
        print('-----------------------------------------------')
        print('| No | Kode Buku |      Nama Buku      | Stok |')
        print('-----------------------------------------------')
        No = 0
        for j in range(i,N):
            if (JB[j] == JenisCari):
                No += 1
                print(f'| {No:>2} | {KB[j]:>9} | {NB[j]:>19} | {Stok[j]:4} |')
        print('-----------------------------------------------')
    else:
        print(f'Jenis buku {JenisCari} tidak ditemukan!')

#subrutin mencari jenis buku menggunakan sequential search dengan boolean
def CariStok(KB,NB,JB,Stok,N):
    #memasukkan stok buku yang dicari
    StokCariMin = int(input('Stok Minimal  : '))
    StokCariMax = int(input('Stok Maksimal : '))
    #proses pencarian
    i = 0
    Ketemu = False
    while (not Ketemu) and (i <= N-1):
        if (Stok[i] >= StokCariMin) and (Stok[i] <= StokCariMax):
            Ketemu = True
        else:
            i += 1

    if (Ketemu):
        os.system('cls')
        print(f'             << PENCARIAN STOK BUKU antara "{StokCariMin} sampai {StokCariMax}" >>')      
        print('-----------------------------------------------------------------------------------')
        print('| No | Kode Buku |      Nama Buku      |               Jenis               | Stok |')
        print('-----------------------------------------------------------------------------------')
        No = 0
        for j in range(i,N):
            if (Stok[j] >= StokCariMin) and (Stok[j] <= StokCariMax):
                No += 1
                print(f'| {No:>2} | {KB[j]:>9} | {NB[j]:>19} | {JB[j]:>33} | {Stok[j]:4} |')
        print('-----------------------------------------------------------------------------------')
    else:
        print(f'Stok buku antara {StokCariMin} sampai {StokCariMax} tidak ditemukan!')

#badan program utama
os.system('cls')
#penciptaan larik kode buku(KB), nama buku(NB), jenis buku(JB) dan stok
KB = ['/'] * MAKSBUKU
NB = ['/'] * MAKSBUKU
JB = ['/'] * MAKSBUKU
Stok = [0] * MAKSBUKU
#penciptaan larik yang dijadikan kloning
KB2 = ['/'] * MAKSBUKU
NB2 = ['/'] * MAKSBUKU
JB2 = ['/'] * MAKSBUKU
Stok2 = [0] * MAKSBUKU

#memasukkan bulan dan tahun
print('PENGISIAN DATA BUKU')
print('===================')
Bulan = str(input('Bulan : ')).upper()
Tahun = str(input('Bulan : '))
TampilBuku(Bulan,Tahun,MAKSBUKU,KB,NB,JB,Stok)
os.system('pause')

os.system('cls')
Menu = 0
Menu = MenuPilihan(Menu)
N = 0
while (Menu != 0):
    os.system('cls')
    match (Menu):
        case 1: #Isi data buku
            N = IsiData(KB,NB,JB,Stok,N)
            TampilBuku(Bulan,Tahun,N,KB,NB,JB,Stok)
            print()
            os.system('pause')
        case 2: #tampil data buku
            if (N > 0):
                TampilBuku(Bulan,Tahun,N,KB,NB,JB,Stok)
            else:
                print('Isi data buku terlebih dahulu!!')
            
            print()
            os.system('pause')
        case 3: #urut data buku
            if (N > 0):
                Keterangan = 'PENGURUTAN'
                Menu2 = 0
                Menu2 = MenuPengurutan(Menu2,Keterangan)
                while (Menu2 != 0):
                    os.system('cls')
                    match (Menu2):
                        case 1: #metode bubble sort ascending
                            UrutKodeAsc(KB,NB,JB,Stok,N)
                            TampilBuku(Bulan,Tahun,N,KB,NB,JB,Stok)
                            print()
                            os.system('pause')
                        case 2: #metode bubble sort descending
                            UrutNamaDsc(KB,NB,JB,Stok,N)
                            TampilBuku(Bulan,Tahun,N,KB,NB,JB,Stok)
                            print()
                            os.system('pause')
                        case 3: #metode maximum sort ascending
                            UrutJenisAsc(KB,NB,JB,Stok,N)
                            TampilBuku(Bulan,Tahun,N,KB,NB,JB,Stok)
                            print()
                            os.system('pause')
                        case 4: #metode Maximum sort descending
                            UrutStokDsc(KB,NB,JB,Stok,N)
                            TampilBuku(Bulan,Tahun,N,KB,NB,JB,Stok)
                            print()
                            os.system('pause')
                        case _: #validasi menu pengurutan
                            print('Nomor Menu Tidak Ada!')
                            print()
                            os.system('pause')

                    os.system('cls')
                    Menu2 = MenuPengurutan(Menu2,Keterangan)
            else:
                print('Isi data buku terlebih dahulu!!')
                print()
                os.system('pause')
        case 4: #cari data buku
            if (N > 0):
                Keterangan = 'PENCARIAN'
                Menu2 = 0
                Menu2 = MenuPengurutan(Menu2,Keterangan)
                while (Menu2 != 0):
                    os.system('cls')
                    match (Menu2):
                        case 1: #cari kode buku menggunakan binary search
                            print('<< PENCARIAN KODE BUKU >>')
                            #kloning data
                            for i in range(N):
                                KB2[i] = KB[i]
                                NB2[i] = NB[i]
                                JB2[i] = JB[i]
                                Stok2[i] = Stok[i]

                            UrutKodeAsc(KB2,NB2,JB2,Stok2,N)
                            CariKodeAsc(KB2,NB2,JB2,Stok2,N)
                            print()
                            os.system('pause')

                            TampilBuku(Bulan,Tahun,N,KB2,NB2,JB2,Stok2)
                            print()
                            os.system('pause')
                        case 2: #cari nama buku (metodenya bebas)
                            print('<< PENCARIAN NAMA BUKU >>')
                            #kerjakan sendiri bagaimana supaya menampilkan nama buku mengandung
                            #nama buku yang dicari, metode searching pilih sendiri
                            
                            print()
                            os.system('pause')

                            TampilBuku(Bulan,Tahun,N,KB,NB,JB,Stok)
                            print()
                            os.system('pause')
                        case 3: #cari jenis buku menggunakan metode sequential search dengan sentinel
                            if (N < MAKSBUKU):
                                print('<<PENCARIAN JENIS BUKU>>')
                                CariJenis(KB,NB,JB,Stok,N)
                                print()
                                os.system('pause')
                                TampilBuku(Bulan,Tahun,N,KB,NB,JB,Stok)
                            else:
                                print('Tempat untuk sentinel tidak ada!')
                            
                            print()
                            os.system('pause')
                        case 4 : #cari stok buku menggunakan metode sequential search dengan boolean
                            print('<<PENCARIAN STOK BUKU>>')
                            CariStok(KB,NB,JB,Stok,N)
                            print()
                            os.system('pause')
                            TampilBuku(Bulan,Tahun,N,KB,NB,JB,Stok)
                            print()
                            os.system('pause')
                        case _: #validasi menu pencarian
                            print('Nomor Menu Tidak Ada!')
                            print()
                            os.system('pause')

                    os.system('cls')
                    Menu2 = MenuPengurutan(Menu2,Keterangan)
            else:
                print('Isi data buku terlebih dahulu!!')
                print()
                os.system('pause')
        case _: #validasi menu pilihan
            print('Nomor Menu Tidak Ada!')
            print()
            os.system('pause')
    
    os.system('cls')
    Menu = MenuPilihan(Menu)