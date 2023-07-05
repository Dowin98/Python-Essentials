# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 18:12:38 2023

@author: Dell
"""

#----------------------------------While Loop----------------------------------
contar=int(input("ingrese el numero al que contare:"))
contador=1
# while contador <= contar:
#     print(contador)
#     contador+=1
    
#Editar con while True 
while True:
    print(contador)
    contador+=1
    if contador > contar:
        break 
    