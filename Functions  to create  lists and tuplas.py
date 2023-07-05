# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 19:54:16 2023

@author: Dell
"""

def lista1(lista):
    for item in lista:
        print("Hola",item)
    print(type(lista))

lista1(["Pepe","Ana","Edwin"])



# cuando se trabaja con el * se la denomida una tupla 
def lista2(*lista1):
    for item in lista1:
        print(item,end=" ")
    print(type(lista1))

lista2(1,2,3,4,5)