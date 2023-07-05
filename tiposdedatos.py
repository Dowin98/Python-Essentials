# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 18:15:13 2023

@author: Dell
"""
#-------------TIPOS DE DATOS ------------------------------
''' # comentar lineas de porgramacion
a=4
b=6.5
c="hola"
d= True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
opt=20/7 #division 
opt2=20//7 #divicion entera 

#----------COMPARACIONES DE OPERACIONES BOOLEAN------------

f= 1>23
print(f)

#---------Operaciones importante solo python---------------
z=5
exp="cisco" *5
print(exp)
print("\n" *2)#salto de linea

#---------Concatenacion-----------------------------------
str1="CEC"
str2="EPN"
str3="Curso python"
spacio=""
print(str1,str2,str3)#uso de coma es str diferentes 

#---------Funciones de conrvercion-----------------------
aa=int()
bb=float()
cc=str()
dd=bool() 

#--------Generar caracteritica de formato-----------------
pi=22/7
print(pi)
print("{:.2f}".format(pi))
print("{:.4f}".format(pi))#imprimir con diferentes decimales 
print("{:.51f}".format(pi))
'''
#--------Diferecia entre lista y tupla-------------------
#En resumen, las tuplas son inmutables y tienen un conjunto
#limitado de operaciones, mientras que las listas son mutables 
#y ofrecen una amplia gama de operaciones para agregar, eliminar 
#y modificar elementos. La elección entre tuplas y listas depende
#de la naturaleza de los datos que deseas almacenar y cómo 
#planeas utilizarlos.


list1=[2,4.5,2, "hola pytohon", True]
list2=[1,2,8,9,6.3,5]

print(list1)
print(type(list1))
print(list1[4])


list1[2]=78
del list1[4]#eliminar pisociones 


#------------------tuplas----------------

tupla=(2,4.5,2, "hola pytohon", True)
print(type(tupla))
print(tupla[0])# llamado a variables dentro del la tupla 

#-----------disccioanrios------------------------
dic1={1:"ID",
      "nombre":"Edwin",
      False:"Matricula",
      "apellido":"Montenegro",
      "email":"dowin_98Qoutllok.com"}
print(dic1[1])# ya le llamo por el indice no por posicion 
dic1["tel"]="0958724275" # añadir 
print("R3" in dic1)# busvar datos en el diccionario 












