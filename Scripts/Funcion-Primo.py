# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 18:13:24 2022

@author: lio
"""

# creamos una funcion para saber si un numero es primo o no segun lo que el usuario ingrese


def isPrime(num):
    divisiones, residuo = 1, 0

    while(divisiones <= num):
        if (num % divisiones) == 0:
            residuo += 1
        divisiones += 1

    if residuo == 2:
        print(f"El numero {num} es primo")
    else:
        print(f"El numero {num} no es primo")

#numero = input("Ingrese un numero para saber si es primo o no: ")
#isPrime(int(numero))

for i in range(0, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()