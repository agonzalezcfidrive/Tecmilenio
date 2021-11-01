import pprint
d1={}
d2=dict()

# Seleccionar muchos renglones, Ctrl + }  para comentar todas las líneas.

# d3={'a':1,
#     'b':2,
#     'c':3,
#     'd':"Hola"
#     }

# print(d3)

d3= {"Usuario":"user123", "correo": "mimail@mio.com","Compañía":"Empresatest"}

d4={1:"uno", 2:"dos", 3:"tres", 4:[1,2,3,4,5,6,7], 5:[1,2,3,4,5,6,7]}
print(d4)

print(d4.keys())
print(d4.values)

pprint.pprint(d3)