import pandas as pd
con = 0
titulo = pd.read_csv('titles.csv')
print(titulo.head(10))
print("\n"*2)
elenco = pd.read_csv('cast.csv')
print(elenco.head(10))
print(titulo[titulo.title.str.contains("war")].sort_values('year'))
print(titulo[titulo.title == "Dracula"].sort_values('year'))
print(titulo[titulo.title.str.contains("The Lord of the Rings")].sort_values('year'))
print(len(titulo[titulo.title.str.contains("The Lord of the Rings")].sort_values('year')))
lista = titulo[titulo.title.str.contains("The Lord of the Rings")].sort_values('year')
print(lista)
for x in lista:
    if "The Lord of the Rings" in x:
        con = con + 1

print(con)