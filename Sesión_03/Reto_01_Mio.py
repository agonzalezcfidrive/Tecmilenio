#def calculadora(operacion, *args)
#    if operacion == "s

# args kwargs
# *args equivale a una tupla (v,v,v,v,)
# def imprimir(*args):
#     for i in args:
#         print(i)
        
# imprimir(1,2,3,4,5,6,7,8,9,10)

# imprimir("hola", "mundo", "como", "estas")

# imprimir(1,2,3,4,5,6,7,8,9,10, "hola", "mundo", "como", "estas")

# print("Hello World", end=",")

def catalogo(**kwargs):
    # print('Hola {} de {}'.format(kwargs['nombre'], kwargs['empresa']))
    for i in kwargs:
        print(i, kwargs[i])
        
        
# catalogo(nombre="Juan", edad=20, pais="Mexico")

dict_catalogo = {"nombre":"Juan", "edad":20, "pais":"Mexico"}
catalogo(**dict_catalogo)

def calculadora(operacion, *args):
    if operacion == "suma":
        print(sum(args))
        
calculadora("suma", 1,2,3,4,5,6,7,8,9,10)