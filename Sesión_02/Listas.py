
# Las listas en Python no pueden cambiar el índice


#Declaración de variables
lista_test=[]
lista_test2= list()

#Declaración de valores
lista_str=["hola", "mundo", "cómo", "estás"]
lista_numero=[1,2,3,4,5,6,7,8,9,10]
lista_float=[1.2,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.10]
lista_bool=[True,False,True,True,False]

lista_mx=(lista_str,lista_numero,lista_float,lista_bool)
lista_mx2=["Hola",159,1.25,True]
#print(lista_mx)


# Cuántos elementos tiene la lista
print(len(lista_mx))

print(type(lista_mx2))

# indices
print(lista_mx2[2])
print(lista_mx2[-1]) # Trae el último elemento

print(lista_str[1:3]) # Trae los valores entre el índice 1 y 3 (el 3ro no está incluido)
print(lista_str[1:]) # Al dejar vacío se trae todos hasta el final

print(lista_numero[0::2]) # Iniciando en el índice 0, hasta el final con intervalo de 2 en 2 (uno si y otro no)
print(lista_numero[1::2]) # Tráe los números pares

lista_str[0]= 1234654
print(lista_str)
lista_str[1:3]=["Otro", "dato"] # Si entre 1 y 3 (como este ejemplo) hay menos espacios que los datos que pasamos, se añaden los elementos y recorren los otros en el índice
print(lista_str)
print(lista_str[2])

lista_str.insert(1,"Adios")
print(lista_str)

thislist= ["apple", "banana", "cherry"]
tropical= ["mango", "pineapple", "papaya", "strawberry", "other"]
thislist.extend(tropical[2:4])
print(thislist)

print(lista_str.pop()) #Elimina y te regresa el último elemento de la lista
print(lista_str)

#  del lista_str  #Borra toda la lista

lista_numero2=[1,5,3,8,5,6,7,2,9,4,10]
# lista_numero2.clear()
print(lista_numero2)

lista_numero2.sort()
print(lista_numero2)
lista_numero2.sort(reverse=True)
print(lista_numero2)