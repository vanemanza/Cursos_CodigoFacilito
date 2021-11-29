# coding: utf-8
"""
a = pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd'], columns=['nombre', 'calificacion'])
a
"""

import pandas as pd
import numpy as np

usuarios = {
    'nombre': ['vane', 'reni', 'faus', 'augus'],
    'calificacion': [8,9,9,9],
    'edad': [46,17,14,11],
    'aprobado': [False, True, True, True],
}

a = pd.DataFrame(usuarios)

print(a)

# podemos definir con q columnas queremos trabajar

a = pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd'], columns=['nombre', 'calificacion'])
print(a)
