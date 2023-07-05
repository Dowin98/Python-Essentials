# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:55:49 2023

@author: Dell
"""

#--------------User Input with conditional elif  ---------------------------------------------------
name=input("Write your first name:")
name2=input("Write your last name:")
age=int(input("how old are you:"))#el input arroja una variable str por lo cual se le cambia a int
address=input("your address: ")


if age >=2 and age <=10:
    print("User information:\n","Full Name:",name,name2,"AGE:",age,"Address:",address,"\n la persona es infantil")
elif age >=10 and age <=15:
    print("User information:\n","Full name:",name,name2,"Age:",age,"Address:",address,"\n la persona es adolecente")
elif age >=15 and age <=25:
    print("User information:\n","Full name:",name,name2,"Age:",age,"Address:",address,"\n la persona es joven")
elif age >=25 and age <=55:
    print("User information:\n","Full name:",name,name2,"Age:",age,"Address:",address,"\n la persona es adulto")
elif age >=60:
    print("User information:\n","Full name:",name,name2,"Age:",age,"Address:",address,"\n la persona es adulto mayor")    
    
