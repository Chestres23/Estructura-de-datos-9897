
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