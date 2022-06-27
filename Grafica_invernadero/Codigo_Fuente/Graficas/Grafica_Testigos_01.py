import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

dt = pd.read_csv('../../Archivos/datosTrue01.csv')
df = pd.DataFrame(dt)
#print(df)

#df.FECHA = pd.to_datetime(df.FECHA, format="%Y/%m/%d")
pd.to_datetime(df.FECHA, format="%Y/%m/%d")

fecha1 = '2022-03-01'
fecha2 = '2022-03-15'

rango = (df.FECHA >= fecha1) & (df.FECHA <= fecha2)
df1 = df.loc[rango]
pd.to_datetime(df1.FECHA, format="%Y/%m/%d")
#print(df1)

aux = None
fch = []
for i in df1.FECHA:
    if i != aux:
        aux = i
        fch.append(i)
#print(fch)


print('Row count is:',len(df1.index))
datos = []
aux = []
df2 = df1
for i in df2:
    if i != 'FECHA':
        for j in range(0, len(fch)):
            rango = (df.FECHA == fch[j])
            df1 = df.loc[rango]
            aux.append(df1[i].mean())
        datos.append(aux)
        aux = []

dtTrue = {'FECHA': fch,
          'T1': datos[0], 'T2': datos[1], 'T3': datos[2], 'T4': datos[3],
          'H1': datos[4], 'H2': datos[5], 'H3': datos[6], 'H4': datos[7],
          'MO1': datos[8], 'MO2': datos[9], 'MO3': datos[10], 'MO4': datos[11],
          'LUX1': datos[12], 'LUX2': datos[13], 'LUX3': datos[14], 'LUX4': datos[15],}

df1 = pd.DataFrame(dtTrue)
pd.to_datetime(df.FECHA, format="%Y/%m/%d")

print(df1)
fig, ax = plt.subplots(2, 2)
ejex = 'FECHA'

ax[0, 0].plot(df1[ejex], df1["T1"], color='blue', label='T1')
ax[0, 0].plot(df1[ejex], df1["T2"], color='orange', label='T2')
ax[0, 0].plot(df1[ejex], df1["T3"], color='green', label='T3')
ax[0, 0].plot(df1[ejex], df1["T4"], color='red', label='T4')
ax[0, 0].legend(loc='upper right')
ax[0, 1].plot(df1[ejex], df1["H1"], color='orange', label='H1')
ax[0, 1].plot(df1[ejex], df1["H2"], color='blue', label='H2')
ax[0, 1].plot(df1[ejex], df1["H3"], color='green', label='H3')
ax[0, 1].plot(df1[ejex], df1["H4"], color='red', label='H4')
ax[0, 1].legend(loc='upper right')
ax[1, 0].plot(df1[ejex], df1["MO1"], color='orange', label='MO1')
ax[1, 0].plot(df1[ejex], df1["MO2"], color='blue', label='MO2')
ax[1, 0].plot(df1[ejex], df1["MO3"], color='green', label='MO3')
ax[1, 0].plot(df1[ejex], df1["MO4"], color='red', label='MO4')
ax[1, 0].legend(loc='upper right')
ax[1, 1].plot(df1[ejex], df1["LUX1"], color='orange', label='LUX1')
ax[1, 1].plot(df1[ejex], df1["LUX2"], color='blue', label='LUX2')
ax[1, 1].plot(df1[ejex], df1["LUX3"], color='green', label='LUX3')
ax[1, 1].plot(df1[ejex], df1["LUX4"], color='red', label='LUX4')
ax[1, 1].legend(loc='upper right')
plt.show()

