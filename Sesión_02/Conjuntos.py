#Sets / conjuntos

s1 = set()

#Requiere llaves para asignar valores
s1= {1,2,3,4,5,6,7,8}

s1.add(550)
print(s1)

s2= {"hola", "mundo", "hola", "mundo","hola", "mundo"}

s1.update(s2)

print(s1)

lista_repetidos=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]

conjunto_resultado=set(lista_repetidos)
print(conjunto_resultado)

set1= {"a", "b", "c"}
set2={1,2,3}
set1.update(set2)
print(set1)

set1.remove("b")
print(set1)
