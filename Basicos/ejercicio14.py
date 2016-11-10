#Autor: guilleCM

#coding=utf-8

#Enunciado:
#Escribe un programa que pida por teclado una cantidad
#de dinero y que a continuación muestre la descomposición 
#de dicho importe en el menor número de billetes y monedas
#de 100, 50, 20, 10, 5, 2 y 1 euro. En el caso de que alguna 
#moneda no intervenga en la descomposición no se tiene que 
#visualizar nada en la pantalla. 

cantidad = int(input("Introduce una cantidad:"))

def contarBilletes(dinero, tipoBillete):
    contador = 0
    while dinero >= tipoBillete:
        dinero = dinero - tipoBillete
        contador += 1
    if contador == 1 and tipoBillete>2:
        print(contador, "billete de", tipoBillete, "euros")
    elif contador == 1 and tipoBillete<=2:
        print(contador, "moneda de", tipoBillete, "euros")
    if contador > 1 and tipoBillete>2:
        print(contador, "billetes de", tipoBillete, "euros")
    elif contador > 1 and tipoBillete<=2:
        print(contador, "monedas de", tipoBillete, "euros")
    cantidad = dinero
    global cantidad
    return cantidad

contarBilletes(cantidad, 100)
contarBilletes(cantidad, 50)
contarBilletes(cantidad, 20)
contarBilletes(cantidad, 10)
contarBilletes(cantidad, 5)
contarBilletes(cantidad, 2)
contarBilletes(cantidad, 1)

#Para una cantidad de 2236 euros 
#la salida que generaría el programa sería:
#==>22 billetes de 100 euros
#==>1 billete de 20 euros
#==>1 billete de 10 euros
#==>1 billete de 5 euros
#==>1 moneda de 1 euro