# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:37:45 2022

@author: lio
"""
print("Ingrese la siguiente informacion..")

nombre = input("Ingrese su Primer Nombre: ")
apellido = input("Ingrese su Primer Apellido: ")
dire = input("Ingrese su direccion de Domicilio: ")
edad = input("Ingrese su edad: ")
space = " "

print(f"\nBIENVENIDO AL SISTEMA.. {nombre}{space}{apellido} has ingresado la informacion al siste tu domicilio es: {dire} y su edad es: {edad}")

"""1-9 niño
10-17 adolescente
18-64 adulto
65 adulto mayor"""

if(int(edad) <= 9 and int(edad) >= 1):
    print("La informacion ingresada es de un niño")
elif(int(edad) <= 17 and int(edad) >= 10):
    print("La informacion ingresada es de un adolescente")
elif(int(edad) <= 64 and int(edad) >= 18):
    print("La informacion ingresada es de un adulto")
elif(int(edad) >= 65):
    print("La informacion ingresada es de un adulto mayor")
else:
    print("Fuera de rango")