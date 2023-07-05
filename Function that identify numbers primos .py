
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 20:20:07 2023

@author: Dell
"""

#-----------------------Funcioens Lambda---------------------------------------

def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
            

    return True
primos=[]
noprimos=[]
for num in range (1,20):
    print("el numero",num,"es",es_primo(num)) 
    if es_primo(num):
        primos.append(num)
    else:
        noprimos.append(num)
        
        
print("por lo tanto los valores son--->",primos,"\n Y los no primos son --->",
      noprimos)
