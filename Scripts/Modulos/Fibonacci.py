# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:13:35 2022

@author: lio
"""

def fibonacci(num):
    while num < 1:
        num = int(input("Ingrese un numero mayor que 1: "))
    
    f1=1
    f2=1
    
    if num == 1:
        print('0')
    elif num == 2:
        print('0','1')
    else:
        print('0',f1,f2,end=" ")
        for i in range(num-3):
            total = f1+f2
            f2 = f1
            f1 = total
            print(total,"",end="")
        
fibonacci(num = int(input("Ingrese un numero mayor que 1: ")))