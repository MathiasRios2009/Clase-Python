nombre = "Mathias"
apellido = "Rios"
nombreCompleto = nombre + " " + apellido
pais = "Ecuador"
ciudad = "Quito"
edad = 15
anio = 2026
estaCasado = False
esVerdadero = True
luzEncendida = False
a, b, c = 1, 2, 3
# actividad 2
print(type(nombre))
print(type(edad))
print(type(estaCasado))
print(len(nombre))
print(len(nombre) > len(apellido))
numeroUno = 5
numeroDos = 4
total = numeroUno + numeroDos
diferencia = numeroUno - numeroDos
producto = numeroUno * numeroDos
division = numeroUno / numeroDos
residuo = numeroDos % numeroUno
potencia = numeroUno ** numeroDos
divisionEntera = numeroUno // numeroDos
print(total, diferencia, producto, division, residuo, potencia, divisionEntera)
import math
radio = 30
areaCirculo = math.pi * radio ** 2
circunferenciaCirculo = 2 * math.pi * radio
print(areaCirculo)
print(circunferenciaCirculo)
radio_usuario = float(input("Ingresa el radio: "))
area = math.pi * radio_usuario ** 2
print("Área:", area)
nombre = input("Nombre: ")
apellido = input("Apellido: ")
pais = input("País: ")
edad = int(input("Edad: "))
print(nombre, apellido, pais, edad)
help('keywords')