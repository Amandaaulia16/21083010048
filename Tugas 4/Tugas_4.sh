#!/bin/bash

read -p "Input: " bilangan
let ganjilgenap=$bilangan%2
a=0
echo ""

if  [ $bilangan -gt $a ]
then
    if [ $ganjilgenap == $a ]
    then
        bilangan=$((bilangan-1))
        while [ $bilangan -gt $a ]
        do
            echo $bilangan
            bilangan=$((bilangan-2))
        done
    else
        while [ $bilangan -gt $a ]
        do
            echo $bilangan
            bilangan=$((bilangan-2))
        done
    fi
else
    echo "Bilangan yang anda masukkan adalah bilangan negatif! Masukkan bilangan positif!"
fi
