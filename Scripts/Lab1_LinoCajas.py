# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:39:34 2022

@author: lio
"""
'''
Su tarea es escribir y probar una función que toma un argumento (un año) y devuelve Verdadero si el año es bisiesto o Falso de lo contrario.
'''

def isYearLeap(year):
    if year <= 0:
        print("Año mal ingresado..")
        return False
    else:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")