#%%numero=int ( input ("Ingrese un numero: 
if numero>0 and numero % 2 == 0: 
    print("El numero es: ", numero, " positivo par") 
elif numero > 0 : 
    print("El numero es: ",numero, " positivo impar") 
elif numero < 0 and numero % 2 == 0 : 
    print("El numero es: ", numero," negativo par ") 
elif numero < 0: 
    print("El numero es: ", numero, " negativo impar") 
else: 
    print("el numero es: 0 ") 
#%%
numero=int(input("Ingrese un numero: "))
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
#%%
edad= int(input("Ingrese su edad")) 
if edad == 18 or edad > 18 :
    print ("mayor de edad")    
else :
    print("menor de edad")
# %%
