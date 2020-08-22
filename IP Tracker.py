import requests
import socket
import colorama
import os
import sys
from colorama import Fore

#Tu IP
ip = 'https://api.ipify.org'
ip2 = requests.get(ip).text

#IP A Rastrear
os.system("cls")
print(f"{Fore.YELLOW}Tu ip: {Fore.RESET}" + (ip2))
target = input(f"{Fore.GREEN}\nTarget IP: {Fore.RESET}")

#Agarra la info de una ip
pais = 'https://ipapi.co/'+(target)+'/country_name'
pais2 = requests.get(pais).text
provincia = 'https://ipapi.co/'+(target)+'/region'
provincia2 = requests.get(provincia).text
ciudad = 'https://ipapi.co/'+(target)+'/city'
ciudad2 = requests.get(ciudad).text
codigopostal = 'https://ipapi.co/'+(target)+'/postal'
codigopostal2 = requests.get(codigopostal).text
numeropais = 'https://ipapi.co/'+(target)+'/country_calling_code'
numeropais2 = requests.get(numeropais).text
moneda = 'https://ipapi.co/'+(target)+'/currency_name'
moneda2 = requests.get(moneda).text
latitud = 'https://ipapi.co/'+(target)+'/latitude'
latitud2 = requests.get(latitud).text
longitud = 'https://ipapi.co/'+(target)+'/longitude'
longitud2 = requests.get(longitud).text
internet = 'https://ipapi.co/'+(target)+'/org'
internet2 = requests.get(internet).text

#Muestra la informacion
os.system("cls") #Limpia la consola
print(f"{Fore.RED} Informacion{Fore.RESET} \n" + "Pais: " + (pais2) + "\nProvincia: " +
 (provincia2) + "\nCiudad: " + (ciudad2) + "\nCodigo Postal: " + (codigopostal2) + "\nCodigo Telefono: " + (numeropais2) + "\nMoneda: " +
 (moneda2) + "\nEmpresa Internet: " + (internet2) + "\nLatitud: " + (latitud2) + "\nLongitud: " + (longitud2))

#Cierra el programa al tocar enter
input(f"{Fore.CYAN}\n¿Queres cerrar el programa? [Enter]: {Fore.RESET}")