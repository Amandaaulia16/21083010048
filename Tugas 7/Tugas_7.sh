#!/bin/bash

echo "==============================="
echo "Menghitung Luas Persegi Panjang"
echo "==============================="

luas_persegi_panjang()
{
    echo -e "\nMasukkan Panjang : "
    read p
    echo -e "\nMasukkan Lebar : "
    read l
    let luas_persegi_panjang=$p*$l
    echo -e "\nLuas Persegi Panjang :  "
    echo $luas_persegi_panjang
}
luas_persegi_panjang
