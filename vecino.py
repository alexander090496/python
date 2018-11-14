# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:29:41 2018

@author: alex
"""

import numpy as np
import matplotlib.pyplot as plt
#%% CREA UNA MATRIZ 5*7 
mat_completa = np.random.randint(100, size = (10, 10))
fil_mat = mat_completa.shape[0]
col_mat = mat_completa.shape[1]
#print("matriz completa \n",mat_completa)
plt.matshow(mat_completa)
plt.show()
#print("filas de la matrix",fil_mat)
#print("cols de la matrix",col_mat)
###############################################################################CREA UNA MATRIZ 3X3 CON CEROS
mascara = np.zeros((3, 3))
mat_filtrada = np.zeros((fil_mat, col_mat))
#print(mascara)



#%%
##################################################################################################FILTRO DE MEDIA_PONDERADA
print("#########################################################################################FILTRO DE MEDIA PONDERADA")

for i in range(fil_mat):
    #print("paso1")
    for j in range(col_mat):
        #print("paso2")
        if (i != 0) and (i != fil_mat-1) and (j != 0) and (j != col_mat-1):
            #print("paso3")
            mascara[0][0] = mat_completa[i-1][j-1]
            #print("esta es la mascara con el dato de la posicion 0,0",mascara[0][0])
            mascara[0][1] = mat_completa[i-1][j]
            mascara[0][2] = mat_completa[i-1][j+1]
            mascara[1][0] = mat_completa[i][j-1]
            mascara[1][1] = mat_completa[i][j] * 2
            mascara[1][2] = mat_completa[i][j+1]
            mascara[2][0] = mat_completa[i+1][j-1]
            mascara[2][1] = mat_completa[i+1][j]
            mascara[2][2] = mat_completa[i+1][j+1]
            #print (mascara)
            promedio = (mascara[0][0] + mascara[0][1] + mascara[0][2] + mascara[1][0] +
            mascara[1][1] + mascara[1][2] + mascara[2][0] + mascara[2][1] + mascara[2][2])/9
            #print ("este es el promedio.......", promedio)
            mat_filtrada[i][j] = int(promedio)
print (mat_filtrada)
plt.matshow(mat_filtrada)
plt.show()

"""
#%%
####################################################################################FILTRO DE MEDIA

print("#########################################################################################FILTRO DE MEDIA")
for i in range(fil_mat):
    for j in range(col_mat):
        if (i != 0) and (i != fil_mat-1) and (j != 0) and (j != col_mat-1):
            mascara[0][0] = mat_completa[i-1][j-1]
            mascara[0][1] = mat_completa[i-1][j]
            mascara[0][2] = mat_completa[i-1][j+1]
            mascara[1][0] = mat_completa[i][j-1]
            mascara[1][1] = mat_completa[i][j]
            mascara[1][2] = mat_completa[i][j+1]
            mascara[2][0] = mat_completa[i+1][j-1]
            mascara[2][1] = mat_completa[i+1][j]
            mascara[2][2] = mat_completa[i+1][j+1]
           # print ("MASCARA \n",mascara)
            promedio = (mascara[0][0] + mascara[0][1] + mascara[0][2] + mascara[1][0] +
            mascara[1][1] + mascara[1][2] + mascara[2][0] + mascara[2][1] + mascara[2][2])/9
            #print ("este es el promedio.......", promedio)
            mat_filtrada[i][j] = int(promedio)
print ("ESTA ES LA MATRIZ FILTRADA \n",mat_filtrada)
plt.matshow(mat_filtrada)
plt.show()
"""

