#Parte A. Análisis y comprensión aplicada (30 puntos)
#1. Análisis de datos y código (15 puntos)
#Observa el siguiente código:
nombre = "Lucía"
edad = 16
promedio = 9.75
cursos = ["Python", "HTML", "CSS"]
print(type(nombre))
print(type(edad))
print(type(promedio))
print(type(cursos))
print(len(nombre))
#Responde:
#a)	1. Str
#2. int
#3. float
#4.list 

 #      b) 
#<class 'str'>
#<class 'int'>
#<class 'float'>
#<class 'list'>
#5
#c)	Explica qué hace len(nombre).
#Este lo que hace es contar el numero de caracteres de la variable nombre que en este caso sería Lucia que tiene 5 caracteres.




#2. Comprensión conceptual (15 puntos)
#Responde con tus palabras:
#a)	¿Qué diferencia hay entre print() e input()?
#La diferencia es que en el input() da paso a que el usuario ósea en Python pueda introducir caracteres para que pueda seguir con el programa en campio el print olo imprime un mensaje que introdusca en programador ya sea una variable o cracteres definidos que puede cambiarsegun el acpmpañante que el print pueda llevar como un len() o un type()
#b)	¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?
#c)	Porque input pide que el usuario de un nueva información mas no calcula eso se podría ahacer con una variable y imprimirlo con un print() que nos permita mostrar mejor lo que se nesecite 
#d)	Explica la diferencia entre /, // y %.
#La primera es una división normal y corriente en la que se incluyen decimales la seunda es una división entera y la otra es el  faltante  de la división 
#e)	Escribe una instrucción que permita comprobar la versión de Python que se está usando.

#f)	Escribe una instrucción que permita consultar las palabras reservadas de Python.


#Parte B. Corrección y construcción de fragmentos (30 puntos)
#3. Corrección de código (15 puntos)
#El siguiente programa tiene errores. Reescríbelo de forma correcta para que funcione.
#Luego responde:
#a)	¿Cuáles eran los errores principales?
#Uno e los errores es que en el código en la parte de los prints había una suma en vesçz de una oa que es lo que sirve para colocar una variable a un lado de un print tambint falta usar float en el uso de los input y falta especificar las variabes
#b)	¿Por qué tu corrección sí permite obtener resultados válidos?
#Porque en el momento de que s realiza una comprobación de los datos este puede realizarse comodamente#

#4. Construcción breve (15 puntos)
#Escribe un fragmento de código que haga lo siguiente:
#1. Cree la variable frase con el texto "Tecnología para todos".
#2. Muestre la frase en mayúsculas.
#3. Muestre la cantidad de caracteres de la frase.
#4. Verifique si la palabra "Python" está dentro de la frase.
#5. Reemplace "Tecnología" por "Programación".
#6. Divida la frase en palabras usando split(). 
texto = "Tecnología para todos"
"""print(f"Frase original: {texto}")
print(texto.capitalize)
print(f"Cantidad de caracteres: {len(texto)}")
python = "Python" in texto
print(f"¿Está 'Python' en la frase?: {esta_python}")
nuevo_texto = texto.replace("Tecnología", "Programación")
print(f"Frase reemplazada: {nuevo_texto}")
palabras = nuevo_texto.split()
print(f"Lista de palabras: {palabras}")"""

#1. Solicite al usuario: Nombre, apellido, país, ancho de la pared, alto de la pared, precio por metro
#cuadrado
#o Calcule: área de la pared, costo total estimado
#2. Cree la variable nombre_completo.
#1. Muestre un reporte final que incluya:
#o nombre completo, país, área calculada, costo total (La impresión del reporte final debe
#realizarse usando f-strings.)
#3. Muestre además:
# nombre_completo en mayúsculas
# la longitud de nombre_completo
# si la letra "a" está presente en nombre_completo
# si el costo total es mayor que 100 

nombre=input("ingrese su nombre:")
apelido=input("ingrese su apellido:")
pais=input("inrese su pais:")
ancho_pared=input("ingrese el ancho de la pared")
alto_pared=input("ingrese el largo de la pared ")
precio_metro=input("ingrese el precio por metro cuadrado")