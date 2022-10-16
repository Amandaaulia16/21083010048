#!/bin/bash

echo "======================================================"
echo "Indeks Prestasi Semester dan Indeks Prestasi Kumulatif"
echo "======================================================"

read -p "Nama : "

read -p "Input Jumlah Semester: " semester

i=0
until [ $i -eq $semester ]
do
    read -p "IP Semester $((i+1)): " IP;
    IPSMahasiswa[$i]=$IP;
    i=$((i+1));
done

j=0
for x in ${IPSMahasiswa[*]}
do
    j=$(printf "$j $x" | awk '{print $1 + $2}');
done

mean=$(printf "$j $semester" | awk '{print $1 / $2}')
echo -e "\nIPS Mahasiswa = $j / $semester"
echo -n "IPK Mahasiswa = "
printf "%.2f" $mean
echo
