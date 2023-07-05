# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:16:02 2023

@author: Dell
"""

#---------------------------------Bucles repetition ------------------------------
lista=["R1","R2","R3",
      "S1","S2","S3",
      "AP1","FW1"]
for elemento in lista:
    print(elemento,end=" ")#impresion vertical de valores de un lista 
    
for i in "Python Ess es en la CEC":#impresion de str con for 
    print(i,end=" ")
    
for item in range(10,20+1,1): # pey atention with the section STOP add+1
    print(item)