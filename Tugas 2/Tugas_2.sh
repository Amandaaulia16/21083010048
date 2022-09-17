#!/bin/bash

header() {
    echo "---------------------"
    echo "      Smart Math     "
    echo "---------------------"
}

header

echo -e "Siapa Namamu?"
read nama
echo "Selamat Datang $nama "

pilihan=("1 Persegi" "2 Persegi Panjang" "3 Segitiga" "4 Lingkaran")

let pilih=$RANDOM%4

echo -e "\nSaya memilih Luas Bangun Datar $pilih, ${pilihan[$pilih]}"
echo -e "\n--------------------------------------------------------"

luas_persegi() {
    header "Menghitung Luas Persegi"
    echo -e "\nMasukkan sisi (cm): "
    read s
    clear
    echo -e "\nsisi = $s cm"
    let luas_persegi=$s*$s
    echo -e "luas_persegi = $luas_persegi cm^2"
}

luas_persegi_panjang() {
    header "Menghitung Luas Persegi Panjang"
    echo -e "\n Masukkan panjang (cm): "
    read p
    echo -e "\n Masukkan lebar (cm): "
    read l
    clear
    echo -e "\n panjang = $p cm"
    echo -e "\n lebar = $l cm"
    let luas_persegi_panjang=$p*$l
    echo -e "\nluas_persegi_panjang = $luas_persegi_panjang cm^2"
}

luas_segitiga() {
    header "Menghitung Luas Segitiga"
    echo -e "\n Masukkan alas (cm): "
    read a
    echo -e "\n Masukkan tinggi (cm): "
    read t
    clear
    echo -e "\n alas = $a cm"
    echo -e "\n tinggi = $t cm"
    luas_segitiga=$(printf "$a $t" | awk '{print 1/2 * $1 * $2}')
    echo -e "\nluas_segitiga = $luas_segitiga cm^2"
}

luas_lingkaran() {
    header "Menghitung Luas Lingkaran"
    echo -e "\n Masukkan jari-jari (cm): "
    read r
    clear
    echo -e "/n jari-jari = $r cm"
    luas_lingkaran=$(printf $r | awk '{print 22/7 * $r * $r}')
    echo -e "luas_lingkaran = $luas_lingkaran cm^2"
}

if [ $pilih == 0 ]
then
    luas_persegi
elif [ $pilih == 1 ]
then
    luas_persegi_panjang
elif [ $pilih == 2 ]
then
    luas_segitiga
else
    luas_lingkaran
fi
