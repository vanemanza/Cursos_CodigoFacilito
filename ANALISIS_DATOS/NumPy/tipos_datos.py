"""
Bool ----- ?
byte(signed) ----- b 
byte(unsigned) ----- B
integer(signed) ----- i 
integer(unsigned) ----- u
float ----- f
complex ----- c
timedelta ----- m
datetime ----- M 
objects ----- O 
Unicode ----- U 

"""

import numpy as np

mi = np.array([1,2,3,4,5,], dtype=np.float32)
print(mi)

"""
indicar el valor de datatype-->
np.array([1,2,3], dtype='f') --> usando un caracter
dtype=float32
o
dtype=np.float32 --> tipo de np
"""