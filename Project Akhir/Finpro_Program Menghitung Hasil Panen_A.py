import os
import time

def home():
    print("|========================================================|")
    print("| 🌾SELAMAT DATANG DI PROGRAM PERHITUNGAN HASIL PANEN🌾  |")
    print("|--------------------------------------------------------|")
    print("|               by AMANDA AULIA (21083010048)            |")
    print("|========================================================|")
    print('\n')
    print("+------------------Perhitungan Hasil Panen---------------+")
    print("|           1. Perhitungan Harga Jual                    |")
    print("|           2. Perhitungan Persentase                    |")
    print("|           0. Keluar                                    |")
    print("+========================================================+")

    p1 = input('Pilih (1/2/0) : ')
    os.system('clear')
    if p1 == '1' :
        hargajual()
    elif p1 == '2' :
        persentase()
    elif p1 == '0' :
        keluar()
    else :
        invalid()
        home()

def keluar() :
    os.system('clear')
    print('{Keluar dari Program  Perhitungan Hasil Panen}')
    time.sleep(0.8)
    os.system('clear')
    exit()

def invalid():
    os.system('clear')
    print('{Pilihan yang Anda Masukkan Tidak Valid}')
    time.sleep(0.8)
    os.system('clear')

def persentase() :
    print("+------------------Perhitungan Persentase----------------+")
    print("|                      1. Buah                           |")
    print("|                      2. Sayur                          |")
    print("|                      0. Kembali                        |")
    print("+========================================================+")

    p1 = input('Pilih (1/2/0) : ')
    os.system('clear')
    if p1 == '1' :
        buah()
    elif p1 == '2' :
        sayur()
    elif p1 == '0':
        home()
    else:
        invalid()
        persentase()

def hargajual() :
    print("+------------------Perhitungan Harga Jual----------------+")
    print("|                      1. Buah                           |")
    print("|                      2. Sayur                          |")
    print("|                      0. Kembali                        |")
    print("+========================================================+")

    p1 = input('Pilih (1/2/0) : ')
    os.system('clear')
    if p1 == '1' :
        buah1()
    elif p1 == '2' :
        sayur1()
    elif p1 == '0':
        home()
    else:
        invalid()
        hargajual()

def buah() :
    print("+---------Perhitungan Persentase Hasil Panen Buah--------+")
    print("|                  1. Alpukat 🥑                         |")
    print("|                  2. Mangga 🥭                          |")
    print("|                  3. Kelapa 🥥                          |")
    print("|                  4. Pisang 🍌                          |")
    print("|                  5. Apel 🍎                            |")
    print("|                  6. Nanas 🍍                           |")
    print("|                  7. Semangka 🍉                        |")
    print("|                  8. Kiwi 🥝                            |")
    print("|                  9. Jeruk 🍊                           |")
    print("|                  0. Kembali                            |")
    print("+========================================================+")
    b = input('Pilih (1/2/.../9/0) : ')
    os.system('clear')
    if b == '1' :
        hitung('Alpukat')
    elif b == '2' :
        hitung('Mangga')
    elif b == '3' :
        hitung('Kelapa')
    elif b == '4' :
        hitung('Pisang')
    elif b == '5' :
        hitung('Apel')
    elif b == '6' :
        hitung('Nanas')
    elif b == '7' :
        hitung('Semangka')
    elif b == '8' :
        hitung('Kiwi')
    elif b == '9' :
        hitung('Jeruk')
    elif b == '0' :
        home()
    else :
        invalid()
        buah()

def buah1() :
    print("+--------------Perhitungan Harga Jual Buah---------------+")
    print("|                  1. Alpukat 🥑                         |")
    print("|                  2. Mangga 🥭                          |")
    print("|                  3. Kelapa 🥥                          |")
    print("|                  4. Pisang 🍌                          |")
    print("|                  5. Apel 🍎                            |")
    print("|                  6. Nanas 🍍                           |")
    print("|                  7. Semangka 🍉                        |")
    print("|                  8. Kiwi 🥝                            |")
    print("|                  9. Jeruk 🍊                           |")
    print("|                  0. Kembali                            |")
    print("+========================================================+")
    b = input('Pilih (1/2/.../9/0) : ')
    os.system('clear')
    if b == '1' :
        hitung1('Alpukat')
    elif b == '2' :
        hitung1('Mangga')
    elif b == '3' :
        hitung1('Kelapa')
    elif b == '4' :
        hitung1('Pisang')
    elif b == '5' :
        hitung1('Apel')
    elif b == '6' :
        hitung1('Nanas')
    elif b == '7' :
        hitung1('Semangka')
    elif b == '8' :
        hitung1('Kiwi1')
    elif b == '9' :
        hitung1('Jeruk1')
    elif b == '0' :
        home()
    else :
        invalid()
        buah1()

def sayur() :
    print("+---------Perhitungan Persentase Hasil Panen Sayur-------+")
    print("|                  1. Padi 🌾                            |")
    print("|                  2. Singkong 🍠                        |")
    print("|                  3. Jagung 🌽                          |")
    print("|                  4. Kentang 🥔                         |")
    print("|                  5. Cabai 🌶                            |")
    print("|                  6. Tomat 🍅                           |")
    print("|                  7. Tebu 🎋                            |")
    print("|                  8. Kacang 🥜                          |")
    print("|                  0. Kembali                            |")
    print("+========================================================+")
    s = input('Pilih (1/2/.../8/0) : ')
    os.system('clear')
    if s == '1' :
        hitung('Padi')
    elif s == '2' :
        hitung('Singkong')
    elif s == '3' :
        hitung('Jagung')
    elif s == '4' :
        hitung('Ketan')
    elif s == '5' :
        hitung('Cabai')
    elif s == '6' :
        hitung('Tomat')
    elif s == '7' :
        hitung('Tebu')
    elif s == '8' :
        hitung('Kacang')
    elif s == '0' :
        home()
    else :
        invalid()
        sayur()

def sayur1() :
    print("+--------------Perhitungan Harga Jual Sayur--------------+")
    print("|                    1. Padi 🌾                          |")
    print("|                    2. Singkong 🍠                      |")
    print("|                    3. Jagung 🌽                        |")
    print("|                    4. Kentang 🥔                       |")
    print("|                    5. Cabai 🌶                          |")
    print("|                    6. Tomat 🍅                         |")
    print("|                    7. Tebu 🎋                          |")
    print("|                    8. Kacang 🥜                        |")
    print("|                    0. Kembali                          |")
    print("|========================================================|")
    s = input('Pilih (1/2/.../8/0) : ')
    os.system('clear')
    if s == '1' :
        hitung1('Padi')
    elif s == '2' :
        hitung1('Singkong')
    elif s == '3' :
        hitung1('Jagung')
    elif s == '4' :
        hitung1('Ketan')
    elif s == '5' :
        hitung1('Cabai')
    elif s == '6' :
        hitung1('Tomat')
    elif s == '7' :
        hitung1('Tebu')
    elif s == '8' :
        hitung1('Kacang')
    elif s == '0' :
        home()
    else :
        invalid()
        sayur1()

def hitung(jenis):
    print('Persentase Keuntungan Hasil Panen', jenis)
    # menginputkan nilai
    print("+--------------------------------------------------------+")
    j_panen = int(input('Jumlah Hasil Panen {} (Kg): '.format(jenis)))
    h_jual = int(input('Harga Jual {} Perkilo     : Rp '.format(jenis)))
    m_awal = int(input('Modal Awal                     : Rp '))
    print("+--------------------------------------------------------+")
    # menghitung total penjualan
    t_penjualan = round(j_panen * h_jual)
    print('Total Penjualan {} : Rp '.format(jenis), t_penjualan)
    print("+--------------------------------------------------------------------------------------+")
    # menghitung persentase keuntungan yang didapat dari penjualan
    p_keuntungan = round(((t_penjualan - m_awal)/m_awal)*100)
    if p_keuntungan > 0 :
        print('Persentase Keuntungan Penjualan {} dengan Harga Penjualan'.format(jenis), 'Rp' , h_jual, 'sebesar'.format(jenis), p_keuntungan, '%')
        print("+--------------------------------------------------------------------------------------+")
    elif p_keuntungan == 0 :
        print('Persentase Penjualan {} dengan Harga Penjualan'.format(jenis), 'Rp' , h_jual, 'sebesar'.format(jenis), p_keuntungan, '%', 'yaitu balik modal')
        print("+--------------------------------------------------------------------------------------+")
    else :
        print('Persentase Kerugian Penjualan {} dengan Harga Penjualan'.format(jenis), 'Rp' , h_jual, 'sebesar'.format(jenis), abs(p_keuntungan), '%')
        print("+--------------------------------------------------------------------------------------+")
    ulang()

def hitung1(jenis):
    print('Harga Penjualan', jenis, 'Perkilo')
    # menginputkan nilai
    print("+--------------------------------------------------------+")
    j_panen = int(input('Jumlah Hasil Panen {} (Kg)             : '.format(jenis)))
    m_awal = int(input('Modal Awal                                  : Rp '.format(jenis)))
    p_keuntungan = int(input('Persentase Keuntungan Penjualan {} (%) : '.format(jenis)))
    print('Persentase keuntungan penjualan {}     :'.format(jenis), p_keuntungan, '%')
    print("+--------------------------------------------------------+")
    # menghitung harga penjual
    t_jual = round(m_awal + ((p_keuntungan/100)* m_awal))
    print('Total Penjualan {}         : Rp'.format(jenis), t_jual)
    print("+--------------------------------------------------------+")
    # menghitung harga jual perkilo
    h_jual = round(t_jual /j_panen)
    print('Harga penjualan {} Perkilo : Rp'.format(jenis), h_jual)
    print("+--------------------------------------------------------+") 
    # final
    print("+----------------------------------------------------------------------------------+")
    print('Harga Penjualan {} Perkilo dengan Persentase Keuntungan'.format(jenis), p_keuntungan, '%', 'sebesar'.format(jenis), 'Rp', h_jual)
    print("+----------------------------------------------------------------------------------+")
    ulang()

def ulang():
    p2 = input('Apakah Anda ingin Menghitung Hasil Panen Lagi?  (y/n) : ').lower()
    os.system('clear')
    if p2 == 'y':
        home()
    elif p2 == 'n':
        keluar()
    else:
        invalid()
        ulang()

if __name__ == '__main__':
    home()
