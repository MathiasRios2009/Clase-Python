numero = int(input("Ingrese un numero: "))
if numero==  0:
        print("el numero es: 0 ")
else :
    if numero>0:
        if numero % 2 == 0:
            print("El numero es: ",numero," positivo par")
        else :
            print("El numero es: ",numero," positivo impar")
    else :
        if numero<0 and numero % 2 == 0:
            print("El numero es: ",numero," negativo par ")
        else :
            print("El numero es: ",numero," negativo impar")
   
   