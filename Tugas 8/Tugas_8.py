from os import getpid, system
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

# Inisialisasi Function
def cetak(i):
    bilangan = i % 2
    if bilangan == 0:
        print(i, "Genap - ID proses", getpid())
    else:
        print(i, "Ganjil - ID proses", getpid())
    sleep(1)

# Input Bilangan
x = int(input("Input : "))

# Sekuensial
print("\nSekuensial")
sekuensial_awal = time()

for i in range(1, x+1):
    cetak(i)

sekuensial_akhir = time()

# Process
print("\nmultiprocessing.Process")
kumpulan_proses = []
process_awal = time()

for i in range(1, x+1):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()

for i in kumpulan_proses:
    p.join()

process_akhir = time()

# Pool
print("\nmultiprocessing.Pool")
pool_awal = time()

pool = Pool()
pool.map(cetak, range(1, x+1))
pool.close()

pool_akhir = time()

# Perbandingan Waktu Eksekusi
print("\nWaktu eksekusi sekuensial              :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool    :", pool_akhir - pool_awal, "detik")
