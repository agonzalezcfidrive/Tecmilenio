# Así se pone un comentario
# int: número entero
# float: número con decimales
# string: cadena de caracteres
# bool: True or False (0,1)

# tipos numéricos
# ejemplo para decir el tipo de dato de la variable  entero:int=4
entero=4
print("El dato introducido contine:")
print(entero)
print("El tipo de dato es:")
print(type(entero))

# tipos flotantes
pi=3.1416
print("El dato introducido contine:")
print(pi)
print("El tipo de dato es:")
print(type(pi))

# tipos string
mensaje="Hola Mundo"
mensaje2='Hola mundo'
mensaje3="""
Este es un
mensaje en varias
líneas
"""
print("El dato introducido contine:")
print(mensaje)
print("El tipo de dato es:")
print(type(mensaje))

# tipos booleanos
bool_variable=True
print("El dato introducido contine:")
print(bool_variable)
print("El tipo de dato es:")
print(type(bool_variable))

# casting
variable=input("Introduce el valor a sumar: ")
print(type(variable))
resultado=5+int(variable)
print("El resultado es:")
print(resultado)
