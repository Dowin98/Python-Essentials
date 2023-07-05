# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:49:51 2023

@author: Dell
"""
#--------------------------sentencias de control-----------------------
listaR=[]#guardar valores de busqueda en una lista 
listaS=[]
listaA=[]
listaF=[]
#--------------------------General List--------------------------------
listaG=["R1","R2","R3",
      "S1","S2","S3",
      "AP1","AP2","AP3",
      "F1","F1","F3"]
#-------------------------create lists about some topics-------
for elemento in listaG:
    if "R" in elemento:# solo se imprimira valores que contengan R 
        print(elemento)
        listaR.append(elemento)#almacenar valores en uan lista 
    elif "S" in elemento:# solo se imprimira valores que contengan S 
        print(elemento)
        listaS.append(elemento)   
    elif "A" in elemento:# solo se imprimira valores que contengan A 
        print(elemento)
        listaA.append(elemento)   
    elif "F" in elemento:# solo se imprimira valores que contengan F
        print(elemento)
        listaF.append(elemento)    
        
    
        