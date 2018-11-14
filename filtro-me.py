# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 18:48:30 2018

@author: alex
"""

def filtro(pixeles,Mceros,fil,col,dicColores):
    dicColores={}
    
    for i in range (fil):
        for j in range(col):
            if Mceros[i,j]==0:
                if i==0:
                    if j==0:
                        if Mceros[i,j+1]!=0:
                            val=pixeles[i,j+1][0]+pixeles[i,j+1][1]+pixeles[i,j+1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i+1,j]!=0:
                            val=pixeles[i+1,j][0]+pixeles[i+1,j][1]+pixeles[i+1,j][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i+1,j+1]!=0:
                            val=pixeles[i+1,j+1][0]+pixeles[i+1,j+1][1]+pixeles[i+1,j+1][2]
                            dicColores[val]=dicColores[val]+1
                    elif j==col-1:
                        if Mceros[i+1,j]!=0:
                            val=pixeles[i+1,j][0]+pixeles[i+1,j][1]+pixeles[i+1,j][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i,j-1]!=0:
                            val=pixeles[i,j-1][0]+pixeles[i,j-1][1]+pixeles[i,j-1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i+1,j-1]!=0:
                            val=pixeles[i+1,j-1][0]+pixeles[i+1,j-1][1]+pixeles[i+1,j-1][2]
                            dicColores[val]=dicColores[val]+1
                    else:
                        if Mceros[i+1,j]!=0:
                            val=pixeles[i+1,j][0]+pixeles[i+1,j][1]+pixeles[i+1,j][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i,j-1]!=0:
                            val=pixeles[i,j-1][0]+pixeles[i,j-1][1]+pixeles[i,j-1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i+1,j-1]!=0:
                            val=pixeles[i+1,j-1][0]+pixeles[i+1,j-1][1]+pixeles[i+1,j-1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i+1,j+1]!=0:
                            val=pixeles[i+1,j+1][0]+pixeles[i+1,j+1][1]+pixeles[i+1,j+1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i,j+1]!=0:
                            val=pixeles[i,j+1][0]+pixeles[i,j+1][1]+pixeles[i,j+1][2]
                            dicColores[val]=dicColores[val]+1
                elif j==0:
                    if i==fil-1:
                        if Mceros[i-1,j]!=0:
                            val=pixeles[i-1,j][0]+pixeles[i-1,j][1]+pixeles[i-1,j][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i,j+1]!=0:
                            val=pixeles[i,j+1][0]+pixeles[i,j+1][1]+pixeles[i,j+1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i-1,j+1]!=0:
                            val=pixeles[i-1,j+1][0]+pixeles[i-1,j+1][1]+pixeles[i-1,j+1][2]
                            dicColores[val]=dicColores[val]+1
                    else:
                        if Mceros[i-1,j]!=0:
                            val=pixeles[i-1,j][0]+pixeles[i-1,j][1]+pixeles[i-1,j][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i,j+1]!=0:
                            val=pixeles[i,j+1][0]+pixeles[i,j+1][1]+pixeles[i,j+1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i-1,j+1]!=0:
                            val=pixeles[i-1,j+1][0]+pixeles[i-1,j+1][1]+pixeles[i-1,j+1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i+1,j+1]!=0:
                            val=pixeles[i+1,j+1][0]+pixeles[i+1,j+1][1]+pixeles[i+1,j+1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i+1,j]!=0:
                            val=pixeles[i+1,j][0]+pixeles[i+1,j][1]+pixeles[i+1,j][2]
                            dicColores[val]=dicColores[val]+1
                elif i==fil-1:
                    if j==col-1:
                        if Mceros[i-1,j]!=0:
                            val=pixeles[i-1,j][0]+pixeles[i-1,j][1]+pixeles[i-1,j][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i,j-1]!=0:
                            val=pixeles[i,j-1][0]+pixeles[i,j-1][1]+pixeles[i,j-1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i-1,j-1]!=0:
                            val=pixeles[i-1,j-1][0]+pixeles[i-1,j-1][1]+pixeles[i-1,j-1][2]
                            dicColores[val]=dicColores[val]+1
                    else:
                        if Mceros[i-1,j]!=0:
                            val=pixeles[i-1,j][0]+pixeles[i-1,j][1]+pixeles[i-1,j][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i,j-1]!=0:
                            val=pixeles[i,j-1][0]+pixeles[i,j-1][1]+pixeles[i,j-1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i-1,j-1]!=0:
                            val=pixeles[i-1,j-1][0]+pixeles[i-1,j-1][1]+pixeles[i-1,j-1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i,j+1]!=0:
                            val=pixeles[i,j+1][0]+pixeles[i,j+1][1]+pixeles[i,j+1][2]
                            dicColores[val]=dicColores[val]+1
                        if Mceros[i-1,j+1]!=0:
                            val=pixeles[i-1,j+1][0]+pixeles[i-1,j+1][1]+pixeles[i-1,j+1][2]
                            dicColores[val]=dicColores[val]+1
                elif j==col-1:
                    if Mceros[i-1,j]!=0:
                        val=pixeles[i-1,j][0]+pixeles[i-1,j][1]+pixeles[i-1,j][2]
                        dicColores[val]=dicColores[val]+1
                    if Mceros[i,j-1]!=0:
                        val=pixeles[i,j-1][0]+pixeles[i,j-1][1]+pixeles[i,j-1][2]
                        dicColores[val]=dicColores[val]+1
                    if Mceros[i-1,j-1]!=0:
                        val=pixeles[i-1,j-1][0]+pixeles[i-1,j-1][1]+pixeles[i-1,j-1][2]
                        dicColores[val]=dicColores[val]+1
                    if Mceros[i+1,j]!=0:
                        val=pixeles[i+1,j][0]+pixeles[i+1,j][1]+pixeles[i+1,j][2]
                        dicColores[val]=dicColores[val]+1
                    if Mceros[i+1,j-1]!=0:
                        val=pixeles[i+1,j-1][0]+pixeles[i+1,j-1][1]+pixeles[i+1,j-1][2]
                        dicColores[val]=dicColores[val]+1
                else:
                    if Mceros[i-1,j]!=0:
                        val=pixeles[i-1,j][0]+pixeles[i-1,j][1]+pixeles[i-1,j][2]
                        dicColores[val]=dicColores[val]+1
                    if Mceros[i,j-1]!=0:
                        val=pixeles[i,j-1][0]+pixeles[i,j-1][1]+pixeles[i,j-1][2]
                        dicColores[val]=dicColores[val]+1
                    if Mceros[i-1,j-1]!=0:
                        val=pixeles[i-1,j-1][0]+pixeles[i-1,j-1][1]+pixeles[i-1,j-1][2]
                        dicColores[val]=dicColores[val]+1
                    if Mceros[i+1,j]!=0:
                        val=pixeles[i+1,j][0]+pixeles[i+1,j][1]+pixeles[i+1,j][2]
                        dicColores[val]=dicColores[val]+1
                    if Mceros[i+1,j-1]!=0:
                        val=pixeles[i+1,j-1][0]+pixeles[i+1,j-1][1]+pixeles[i+1,j-1][2]
                        dicColores[val]=dicColores[val]+1
                    if Mceros[i+1,j+1]!=0:
                        val=pixeles[i+1,j+1][0]+pixeles[i+1,j+1][1]+pixeles[i+1,j+1][2]
                        ##
                        dicColores[val]=dicColores[val]+1
                    if Mceros[i,j+1]!=0:
                        val=pixeles[i,j+1][0]+pixeles[i,j+1][1]+pixeles[i,j+1][2]
                        dicColores[val]=dicColores[val]+1
                    if Mceros[i-1,j+1]!=0:
                        val=pixeles[i-1,j+1][0]+pixeles[i-1,j+1][1]+pixeles[i-1,j+1][2]
                        dicColores[val]=dicColores[val]+1
    return (dicColores)
    
    clave_mayor = max(dicColores.keys())
    mayor=dict.get(clave_mayor)
    print("dato mayor", mayor)
    
    ###faltaria encontrar el valor que mas se repite
    #recorrer diccolores y saber cual es el que mas se repite
    #asignarle a pixeles en la posicion i,j el valor que ms se repitio
    #reiniciar diccolores
    #retorno pixeles
    #asigna a pixeles la posision ij la que mas se repitio y verificar que sea diferente de cero 
                    
                    
                    
                    
                    
                    
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        