print("Hola mundo..")
a = 5
print(a)

pi = 2/7
print(pi)
# el limite es 51
print("{:.51f}".format(pi))

# listas en python
miLista = [10, 2, 5.33]
print(miLista)
print(len(miLista))
# sort solo sirve para numeros o letras pero no una mezcla
miLista.sort()
print(miLista)
v1="A"
v2="b"
v3="c"
#el operador + concatena pero la , separa
print(v1+v2+v3)
print(v1,v2,v3)
print("asdasd",a)
#input
nombr = input("Ingrese su nombre:")
print("Hola "+nombr)
#uso del for
for item in miLista:
    print(item)