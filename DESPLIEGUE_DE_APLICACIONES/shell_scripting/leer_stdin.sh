#!/bin/bash

read -p "Ingresa tu nombre" nombre

echo "Ingresa tu edad:"
read edad

read -sp "Ingresa tu contraseña:" password
echo "\n"
echo "Hola" $nombre "tu edad es" $edad "años"
echo $password
