#Autor: guilleCM

#coding=utf-8

#Enunciado:
#funciones para comparar que numeros son mas grandes

def bigger(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

def biggest(n1,n2,n3):
    return bigger(n1, bigger(n2,n3))
