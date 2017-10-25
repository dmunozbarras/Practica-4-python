# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 4 - EJERCICIO 2
Escriu un programa que demani dos nombres i escrigui quins nombres son parells
i quins són senars impares des del primer fins al segon"""

print("PARES E IMPARES")
num1 = int(input("Escriba un numero entero: "))
num2 = int(input("Escriba un número entero mayor que %d: " % (num1)))

if num2<=num1:
    print "No has introducido un numero mayor que el primero"

else:
    for i in range (num1, num2+1):
        if i %2 == 0:
            print 'El numero %d es par' % (i)
        else:
            print 'El numero %d  es impar' % (i)
