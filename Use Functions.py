# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 18:54:36 2023

@author: Dell
"""

#---------------------------------Functions-------------------------------------
'''
def message():#definate the function 
    print("Enter a value: ")
message()#call the function 
a=input()
message()
b=input()
message()
c=input()
message()
d=input()

def  greeting(nombre="CEC-EPN"):#define the function with parameters
     #Of course, the parameters could be defined
    print("Hola",nombre)
    
greeting("Ana")
greeting("Edwin")
greeting("Ana")
greeting()
'''

def greeting2(nombre,apellido):#define the function with  Two parameters
    print("Hola",nombre,apellido)
    
greeting2("edwin", "Montenegro")


def delivery(ciudad,barrio,calle):
    print("la entrega esta en:",ciudad)
    print("El barrio en:",barrio)
    print("esperar en:",calle)
    print("\n"*2)    
ci=input("Ingrese la ciudad:")
ba=input("Ingrese el sector:")
ca=input("Ingrese la referenciaa:")


delivery(ci, ba, ca)