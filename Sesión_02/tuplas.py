t1=()
t2=tuple()

# Tupla de un elemento
t3=(1,)  # se tiene que especificar que es tupla al dejar un elemento y otro vacío cuando sólo se tiene un dato.

a,b= (1,2)

print(a+150, b-548)

t3=tuple(range(1,10))

print(t3)

test_nose_que_algo=("hola","como","estas")
print(type(test_nose_que_algo))


lista_resultado=list(test_nose_que_algo[0:2])
print(type(lista_resultado))
print(lista_resultado)
