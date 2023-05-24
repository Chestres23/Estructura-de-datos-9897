
lista = []
print(type(lista))

lista = [1,2,3,4]
print(lista)

lista = ["Diego", True, 3.14, 3, 4j, ["a", "b"], 4]
print(lista)

lista.append("Chris")
print(lista)

lista2 = lista.copy()
print(lista2)

lista2.clear()
print(lista2)

lista2 = ["a","e","e","i","o","u"]
print(lista2.count("e"))

print(len(lista2))

print(lista2[4])
print(lista2[5])

lista2.pop()
print(lista2)

lista2.remove("a")
print(lista2)

lista2.sort()
print(lista2)

lista2 = ["a","b","B","c","d"]
lista2.sort()
print(lista2)

#TUPLA

tupla = ("Quito","Guayaquil","Cuenca","Quito")
print(type(tupla)) #No se pueden modificar

# tupla.append("Machala")
# print(tupla) 

print (tupla.count("Quito"))
print (tupla.index("Cuenca"))
# print (tupla.index("Quito"))

lista = list(tupla)
print(lista)
print(tupla)

lista.append("Machala")
tupla = tuple(lista)

print(lista)
print(tupla)

#RANGO

rango = range(10)
print (type(rango))
print (rango)

#SETS

conjunto = {"i","e", "u", "o", "i", "a"}
print(type(conjunto))
print(conjunto)

#DICCIONARIOS

cliente001 = {}



