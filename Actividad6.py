# for in range 
desde=int(input('ingrese dese que numero quiere: '))
hasta=int(input('ingrese el numero hasta donde quiera: '))
num=int(input('ingrese un numero: '))
for i in range(desde,hasta+1):
    por=num*i
    print(f'{num}x{i}={por}')
