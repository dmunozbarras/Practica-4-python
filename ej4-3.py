# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 4 - EJERCICIO 3
Escriu un programa que demani 2 nombres i escrigui la suma de sencers des del primer nombre
fins al segon."""

print("SUMA DE ENTEROS")
num1 = int(input("Escriba un numero entero: "))
num2 = int(input("Escriba un número entero mayor que %d: " % (num1)))

if num2<=num1:
    print "No has introducido un numero mayor que el primero"

else:
    suma = 0
    for i in range (num1, num2+1):
        suma=suma+i
        print(i)
        print "La suma es %d" % (suma)
