# Importar módulos desde la librería estandar

import os
import pprint
files = os.listdir()
print(files)

pprint.pprint(files)


size = os.path.getsize ('01_funciones.py')
print(size)