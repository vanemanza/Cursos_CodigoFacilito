# coding: utf-8
pd.Series([10,20,30,40,50])
a = pd.Series([10,20,30,40,50])
a
import numpy as np
a = pd.Series([10,20,30,40,50], dtype=np.float32)
a
a[0]
a[a.size-1]
a[0] = 90
a
a = pd.Series([10,20,30,40,50], dtype=np.float32, index=['a', 'b', 'c', 'd', 'e'])
a
a[1]
a['a']
a['b']
a[1]
a[['a', 'c']]
diccionario = {
'a':10,
'b':200,
'c':3000}
b = pd.Series(diccionario)
b
b['a']
