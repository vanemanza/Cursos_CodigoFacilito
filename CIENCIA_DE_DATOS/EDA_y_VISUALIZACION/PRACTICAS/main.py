import os

import numpy as np
import pandas as pd

# 1) CARGAR LOS DATOS:
"""
Cargar datos significa convertir los datos que 
están en un formato genérico (csv, json, etc), 
los vamos a trabajar con Pandas.
"""
country_codes = []
# os.walk se usa para recorrer directorios

for dirname, _, filenames in os.walk('../data/trending_youtube/'):
    for filename in filenames:
        print(os.path.join(filename))
        code = filename[:2]
        if not (code in country_codes) and code.isalpha() and code.isupper():
            country_codes.append(code)
country_codes.sort()
print(country_codes)

#---------------------------------------------------------------------------------

# 2) LEER LOS DATOS:
df_countries = {}
route = "../data/trending_youtube/"
for code in country_codes:
    print(f"Processing {code}")
    df_countries[code] = pd.read_csv(f"{route}{code}videos.csv", delimiter=',')

#from datetime import datetime
#df_countries['trending_date'] = df_countries['trending_date'].date   
"""  
for pais in df_countries:
    t_date = str(df_countries[pais]['trending_date'])
    date_object = datetime.strptime(t_date, '%y %d, %m')
    print(date_object)
"""
#---------------------------------------------------------------------------------

# 3) CONECTAR CON SQLITE3:

import sqlite3

conn = sqlite3.connect(f'{route}trendingMX.db') #hace la conexion y crea el archivo de la db
cursor = conn.cursor() # es el objeto a traves del cual le paso comandos al motor de db
cursor.execute('''
CREATE TABLE IF NOT EXISTS TrendingMX
(video_id TEXT, trending_date TEXT, likes INT, dislikes INT)
''') # crea una tabla con 4 campos
conn.commit()
conn.close()

#---------------------------------------------------------------------------------

# 4) GUARDANDO LOS DATOS EN FORMATO PARQUET

route = "../data/trending_youtube/"
for code in country_codes:
    print(f"Processing {code}")
    df_countries[code].to_parquet(f"{route}{code}videos.parquet")

"""
formato de datos tabulares  --> excel
                            --> csv
                            --> parquet

formato de datos jerarquicos --> json                            
"""


