#!/bin/bash

read -p "ingresa tu username: " username

read -p "edad : " edad

# ()
# (( ))
# []
# [[ ]]
# str == o !=
# int > < >= pero es mejor con comandos:
#gt-lt-ge-le-eq-ne todos con el prefijo -
if [[ $username == "Cody"  ]]
then
	echo "Hola cody"
else
	echo "hola usuario" $username
fi

if [[ $edad > 18 ]]
then 
	echo "puedes"
else
	echo "no puedes"
fi
