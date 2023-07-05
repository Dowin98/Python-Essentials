# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:31:20 2023

@author: Dell
"""
'''
# -------------------How can use the conditional IF--------------------
print("Inicio")

a=int(input("Add a number:"))
b=int(input("Add a number:"))
if a==b:
    print("The numbers are same")
elif a!=b:
    print("The numbers are diferents ")
elif a >= b:
    print("a is more big than b")
else: 
    print(" b is more big than a")
    
print("Fin")
'''

#--------------------------How can use the conditional  elif--------------------

acl= int(input("ingrese el # de ACL:"))
if acl >= 1 and acl <=99:
    print("las ACL es estandar")
elif acl >= 100 and acl <=199:
    print("la ACL es extendidad ")
else:
    print("el # ingresado no es un CL")