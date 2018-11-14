# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
#%% Librerias necesarias

from PIL import Image                #librería para el manejo de imágenes
import numpy as np                   #librería para el manejo de matrices
import matplotlib.pyplot as plt      #librería para graficar sobre la consola de python
from osgeo import gdal
import struct
from os import listdir
#from colorama import Fore, init

#%% Funcion para obtener los datos del pixel en formato matriz, retorna la matriz
#   y el número de filas y columnas

def matrizHDF(archivoModisHdf):
    #Archivo = "d:/MOD09GA.A2010091.h10v08.006.2015206012214.hdf"
    hdf_file = gdal.Open(archivoModisHdf)
     
    subDatasets = hdf_file.GetSubDatasets()
     
    dataset = gdal.Open(subDatasets[0][0])
    geotransform = dataset.GetGeoTransform()
    band = dataset.GetRasterBand(1)
     
    fmttypes = {'Byte':'B', 'UInt16':'H', 'Int16':'h', 'UInt32':'I', 
                'Int32':'i', 'Float32':'f', 'Float64':'d'}
    ####
    filas=band.YSize
    columnas=band.XSize
    print ("rows = %d columns = %d" % (filas, columnas))
     
    BandType = gdal.GetDataTypeName(band.DataType)
     
    print ("Data type = ", BandType)
     
    print ("Executing with %s" % archivoModisHdf)
     
    print ("test_value = 256")
     
    #X = geotransform[0] #x coordinate
    #Y = geotransform[3] #y coordinate
    
    m=np.empty((filas, columnas))
    
    for y in range(band.YSize):
        scanline = band.ReadRaster(0, y, band.XSize, 1, band.XSize, 1, band.DataType) 
        #print (scanline)
        values = struct.unpack(fmttypes[BandType] * band.XSize, scanline)
        #print (values)
        pixeles= np.asarray(values)
        #print("pixeles",pixeles)
        for i in range(columnas):
            m[y,i]=pixeles[i]
    """
    print(values)
    pixeles= np.asarray(values)
    print(m[2223,2482])
    """
    dataset = None
    return (m,filas,columnas)
    
#%%   Función para determinawr el color adecuado de pixel según datos de Modis

def rgbmap(pixel):
    Cs = pixel & 3
    if Cs == 1:
        P=0
        R=0
        G=0
        B=0
    else :
        P=1
        #print(Cs)
        Pixel2=pixel>>2
        Csh=Pixel2&1
        f1=0;
        if Csh == 1:
            f1 =-20
        
        #print(Csh)
        Pixel3=Pixel2>>1
        lwf=Pixel3&7
        
        if lwf ==0:
            #oceano poco profundo
            R=161
            G=242
            B=255
        elif lwf==1:
            #Tierra zonas verdes
            R = 0
            G = 64
            B = 7
        elif lwf==2:
            #Costa Oceano o lago
            R = 241
            G = 182
            B = 71
            ##494
        elif lwf == 3:
            # Aguas internas poco profundas
            R = 208
            G = 240
            B = 251
            #699
        elif lwf == 4:
            #Aguas efimeras
            R = 171
            G = 218
            B = 218
            
            #607
        elif lwf == 5:
            # aguas interiores poco profundas
            R = 254
            G = 230
            B = 179
            #663
        elif lwf == 6:
            # oceano contineltal moderado
            R = 68
            G = 144
            B = 211
            #423
        elif lwf == 7:
            # oceano profundo
            R = 52
            G = 87
            B = 189
            #328
                    
        R=R+f1
        G=G+f1
        B=B+f1
    
    return (R,G,B,P)

#%% Programa Principal

#f=Image.open("d:/relieve.jpg")
#pixelesf = f.load()7
"""
ar=[]
for li in listdir("C:/Users/alex/Documents/Tesis/12-08-2018/modisRecorte"):
    ar.append(li)

for nom in ar:
    """
Archivo = "C:/Users/alex/Documents/Tesis/12-08-2018/modisRecorte/MOD09GA.A2010003.h10v08.006.2015198061449.hdf"
#Archivo = "d:/MOD09GA.A2018028.h10v09.006.2018030025537.hdf"
#t=f.size                             #retorna un vector con la cantidad de columnas y filas de la imagen f
(modis,fil,col) = matrizHDF(Archivo)
#g = Image.new( 'RGB', (t[0],t[1]), "black") # create a new black image
g = Image.new( 'RGB', (fil,col), "black") # create a new black image
pixelesg = g.load()
#print("este es la nueva imagen \n ",g)

#dato_pixel = f.getpixel((1, 1))

#%%
M=np.ones((fil,col))
dicColores={}##se define diccionario de colores

for i in range(fil):    # for every col:
    for j in range(col):    # For every row
        #rgb=pixelesf[i,j]      
        colores=rgbmap(int(modis[i,j]))
        if colores[3]==0:
            M[i,j]=0
            
            
        rf=colores[0]
        gf=colores[1]
        bf=colores[2]
        #bf=255-rgb[2]
        pixelesg[i,j] = (rf,gf,bf) #pixelesf[i,j]#=(i, j, 100) # set the colour accordingly
        dicColores[rf+gf+bf]=0

#print(f.mode)
#print("columnas:",t[0]," Filas:",t[1])  #Cantidad de columnas
#print(dato_pixel)

#plt.imshow(np.asarray(f))
plt.show()
plt.imshow(np.asarray(g))


#g.show()

#f.close()
#g.close()

#%%
"""
def filtro():
    mascara = np.zeros((3, 3))
    f = Image.new( 'RGB', (fil,col), "black")
    pixelesf=f.load()
    #ng=np.asanyarray(g)
    print("inicio-- \n",pixelesf)
    print("matriz de ceros 3x3 \n",mascara)
    print("#########################################################################################FILTRO ")
    for i in range(2,fil-3):
        ####################print("paso1")
        for j in range(2,col-3):
            #print("paso2")
            #if (i != 0) and (i != fil-1) and (j != 0) and (j != col-1):
                #print("paso3")
                
                mascara[0][0] = pixelesg[i-1,j-1]
                mascara[0][1] = pixelesg[i-1,j]
                mascara[0][2] = pixelesg[i-1,j+1]
                mascara[1][0] = pixelesg[i,j-1]
                mascara[1][1] = pixelesg[i,j] * 2
                mascara[1][2] = pixelesg[i,j+1]
                mascara[2][0] = pixelesg[i+1,j-1]
                mascara[2][1] = pixelesg[i+1,j]
                mascara[2][2] = pixelesg[i+1,j+1]
                #print (mascara)
                promedio = (mascara[0][0] + mascara[0][1] + mascara[0][2] + mascara[1][0] +
                mascara[1][1] + mascara[1][2] + mascara[2][0] + mascara[2][1] + mascara[2][2])/9
                
                rgb1=pixelesg[i-1,j-1]
                rgb2=pixelesg[i-1,j]
                rgb3=pixelesg[i-1,j+1]
                rgb4=pixelesg[i,j-1]
                rgb5=pixelesg[i,j] * 2
                rgb6=pixelesg[i,j+1]
                rgb7=pixelesg[i+1,j-1]
                rgb8=pixelesg[i+1,j]
                rgb9=pixelesg[i+1,j+1]
                fr = int((rgb1[0]+rgb2[0]+rgb3[0]+rgb4[0]+rgb5[0]+rgb6[0]+rgb7[0]+rgb8[0]+rgb9[0])/9)
                fg = int((rgb1[1]+rgb2[1]+rgb3[1]+rgb4[1]+rgb5[1]+rgb6[1]+rgb7[1]+rgb8[1]+rgb9[1])/9)
                fb = int((rgb1[2]+rgb2[2]+rgb3[2]+rgb4[2]+rgb5[2]+rgb6[2]+rgb7[2]+rgb8[2]+rgb9[2])/9)
                
                print ("r1------------","R= ",rgb1[0]," G= ",rgb1[1],"B= ",rgb1[2] )
                print ("r2------------","R= ",rgb2[0]," G= ",rgb2[1],"B= ",rgb2[2] )
                print ("r3------------","R= ",rgb3[0]," G= ",rgb3[1],"B= ",rgb3[2] )
                print ("r4------------","R= ",rgb4[0]," G= ",rgb4[1],"B= ",rgb4[2] )
                
                pixelesf[i,j]=(fr,fg,fb)
    

###############################################################################CREA UNA MATRIZ 3X3 CON CEROS
mascara = np.zeros((3, 3))
f = Image.new( 'RGB', (fil,col), "black")
pixelesf=f.load()
#ng=np.asanyarray(g)

print("inicio-- \n",pixelesf)
print("matriz de ceros 3x3 \n",mascara)
print("#########################################################################################FILTRO ")
for i in range(2,fil-3):
    ####################print("paso1")
    for j in range(2,col-3):
        #print("paso2")
        #if (i != 0) and (i != fil-1) and (j != 0) and (j != col-1):
            #print("paso3")
            
            mascara[0][0] = pixelesg[i-1,j-1]
            mascara[0][1] = pixelesg[i-1,j]
            mascara[0][2] = pixelesg[i-1,j+1]
            mascara[1][0] = pixelesg[i,j-1]
            mascara[1][1] = pixelesg[i,j] * 2
            mascara[1][2] = pixelesg[i,j+1]
            mascara[2][0] = pixelesg[i+1,j-1]
            mascara[2][1] = pixelesg[i+1,j]
            mascara[2][2] = pixelesg[i+1,j+1]
            #print (mascara)
            promedio = (mascara[0][0] + mascara[0][1] + mascara[0][2] + mascara[1][0] +
            mascara[1][1] + mascara[1][2] + mascara[2][0] + mascara[2][1] + mascara[2][2])/9
            
            rgb1=pixelesg[i-1,j-1]
            rgb2=pixelesg[i-1,j]
            rgb3=pixelesg[i-1,j+1]
            rgb4=pixelesg[i,j-1]
            rgb5=pixelesg[i,j] * 2
            rgb6=pixelesg[i,j+1]
            rgb7=pixelesg[i+1,j-1]
            rgb8=pixelesg[i+1,j]
            rgb9=pixelesg[i+1,j+1]
            fr = int((rgb1[0]+rgb2[0]+rgb3[0]+rgb4[0]+rgb5[0]+rgb6[0]+rgb7[0]+rgb8[0]+rgb9[0])/9)
            fg = int((rgb1[1]+rgb2[1]+rgb3[1]+rgb4[1]+rgb5[1]+rgb6[1]+rgb7[1]+rgb8[1]+rgb9[1])/9)
            fb = int((rgb1[2]+rgb2[2]+rgb3[2]+rgb4[2]+rgb5[2]+rgb6[2]+rgb7[2]+rgb8[2]+rgb9[2])/9)
            
            print ("r1------------","R= ",rgb1[0]," G= ",rgb1[1],"B= ",rgb1[2] )
            print ("r2------------","R= ",rgb2[0]," G= ",rgb2[1],"B= ",rgb2[2] )
            print ("r3------------","R= ",rgb3[0]," G= ",rgb3[1],"B= ",rgb3[2] )
            print ("r4------------","R= ",rgb4[0]," G= ",rgb4[1],"B= ",rgb4[2] )
        
            pixelesf[i,j]=(fr,fg,fb)

            
                
print("contador de negros 1",c1,[i,j])
print("contador de negros 2",c2,[i,j])
print("contador de negros 3",c3)
print("contador de negros 4",c4)
print("contador de negros 5",c5)
print("contador de negros 6",c6)
print("contador de negros 7",c7)
print("contador de negros 8",c8)
print("contador de negros 9",c9)
                
            ###############################################################################################################aqui bota el error
            
            #pixelesf[i,j] = promedio
            ################################################################################################################
            #print("nueva imagen estos son los pixeles",mat_filtrada[i,j])
#print ("final---\n ",pixelesf)
plt.show()
plt.imshow(np.asarray(f))

#f.show()
"""