# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:31:29 2022

@author: lio
"""


def readint(prompt, min, max):
    try:
        num = int(prompt)
        if not (num >= min and num <= max):
            return f"el valor no está en el rango permitido {min} - {max}"
    except ValueError:
        return "Error en el ingreso"
    else:
        return num


v = readint("asd", -10, 10)

print("The number is:", v)
