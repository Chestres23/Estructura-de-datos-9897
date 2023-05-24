primerNumero = 4
segundoNumero = 5

print(primerNumero + segundoNumero)

# Codigo Correcto

primerNumero = input("Ingrese el primer número: ")
segundoNumero = input("Ingrese el segundo número: ")

primero = int(primerNumero)
segundo = int (segundoNumero)

print(primero + segundo)

# Agregando una validacion

primerNumero = input("Ingrese el primer número: ")

try:
    primero = int(primerNumero)
except:
    primero = "Cadena"

segundoNumero = input("Ingrese el segundo número: ")

try:
    segundo = int(segundoNumero)
except:
    segundo = "Cadena"

if primero == "Cadena" or segundo == "Cadena":
    print ("Ingreso mal de un dato, ingrese unevamente")
else:
    print (primero + segundo )

