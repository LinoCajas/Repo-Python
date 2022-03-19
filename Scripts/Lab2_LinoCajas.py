# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 20:04:26 2022

@author: lio
"""
'''
Su tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días para el par mes / año dado (aunque solo febrero es sensible al valor del año, su función debería ser universal).
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

def daysInMonth(year, month):
    if year < 1582 or year <= 0 or month < 1 or month > 12 or month <= 0:
        print("Mes mal ingresado..")
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and isYearLeap(year):
        res = 29
    return res

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
