#Autor: guilleCM y Luis Cifre

#coding=utf-8



def resolverEquacionSegundoGrado (a, b, c):
    import math

interiorRaiz = b**2 -(4*a*c)
    if interiorRaiz >= 0:
        resultadoRaiz = math.sqrt(interiorRaiz)
        x1 = (-b + resultadoRaiz) / 2*a
        x2 = (-b - resultadoRaiz) / 2*a
        if x1 == x2:
            x = x1
            return x
        else:
            return x1, x2
    else:
            return NONE


###CASOS TEST###
print (resolverEquacionSegundoGrado (1, -4, 4))