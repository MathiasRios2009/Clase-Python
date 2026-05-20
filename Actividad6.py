# for in range 
desde=int(input('ingrese dese que numero quiere: '))
hasta=int(input('ingrese el numero hasta donde quiera: '))
num=int(input('ingrese un numero: '))
for i in range(desde,hasta+1):
    por=num*i
    print(f'{num}x{i}={por}')

notas=[5, 9, 4, 5, 10]
suma=0
for i in range(1,4):
    suma=suma+notas[i]
promedio=suma/3
print(f"El promedio es: {promedio}")
