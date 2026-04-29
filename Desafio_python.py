nombre=input("ingrese su nombre: ")
edad=int(input("ingrese su edad "))
puntaje=int(input("Ingrese su puntaje: "))
asistencia=int(input("ingrese su cantidad de asistencias: "))
codigo_invitacion=input("ingrese su codigo de invitacion ")
promedio=(puntaje+asistencia)/2
if edad >= 14:
    if promedio >= 80 and codigo_invitacion == "PYTHON 2026":
        print("Acceso VIP")
    else: 
        print("Acceso General")
    if promedio >60 :
        print("Acceso con observación")
    else:
        print("No puede ingresar por bajo rendimiento")
else:
    if codigo_invitacion == "PYTHON 2026":
        print("Acceso especial con acompañante")
    else: 
        print("No cumple la edad mínima")
if puntaje >90 and asistencia >= 90:
    print("Candidato destacado")
elif puntaje< 50 and asistencia<50: 
    print("Requiere refuerzo previo")
#mENSAJES ADICIONALES
print("Participante: ",nombre.upper )
print(" Caracteres del nombre:",len(nombre))
print("Promedio general: ", promedio)
print("Resultado: Acceso vip")
print(" Mensaje adicional: ")
