print("------Ejercio 1-------")
notas = [8.5, 6.0, 9.0, 7.0, 5.5]
suma = 0
aprobados = 0
reprobados = 0
cantidad = 0

for nota in notas:
    suma = suma + nota
    cantidad = cantidad + 1

    if nota >= 7:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

promedio = suma / cantidad

print("Suma total:", suma)
print("Promedio:", promedio)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)

print("------Ejercio 2: Strings-------")

contrasena = "Python2026"
numeros = 0
cantidad_o = 0

for caracter in contrasena:

    if caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9":
        numeros = numeros + 1

    if caracter == "o":
        cantidad_o = cantidad_o + 1

letras = len(contrasena) - numeros

print("Cantidad de letras:", letras)
print("Cantidad de números:", numeros)
print("Cantidad de veces que aparece 'o':", cantidad_o)

print("------Ejercio 3: Set -------")



productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}

cantidad_productos = 0
mas_6_letras = 0

for producto in productos:

    cantidad_productos = cantidad_productos + 1

    contador = 0

    for letra in producto:
        contador = contador + 1

    if contador > 6:
        mas_6_letras = mas_6_letras + 1

print("Productos únicos:", cantidad_productos)
print("Productos con más de 6 letras:", mas_6_letras)

print("------Ejercicio 4: Break------")

correo = input("Ingrese su correo electrónico: ")

usuario = ""

for caracter in correo:

    if caracter == "@":
        break

    usuario = usuario + caracter

print("Nombre de usuario:", usuario)
