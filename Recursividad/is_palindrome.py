#Autor: guilleCM 

#coding=utf-8

# Enunciado:
# Define a procedure is_palindrome, that takes as input a string,
# and returns a Boolean indicating if the input string is a palindrome.

def is_palindrome(s):
    espejoString = ""
    contador =  len(s) - 1
    while contador >= 0:
        espejoString = espejoString + s[contador]
        contador -= 1
    if espejoString == s:
        return True
    else:
        return False
 
 
#CASOS TEST# 
#print is_palindrome('')
#>>> True
#print is_palindrome('abab')
#>>> False
#print is_palindrome('abba')
#>>> True