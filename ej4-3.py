# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 4 - EJERCICIO 3
Escriu un programa que demani 2 nombres i escrigui la suma de sencers des del primer nombre
fins al segon."""

print("SUMA DE ENTEROS")
num1 = input("Escriba un numero entero: ")
num2 = input("Escriba un número entero mayor que %d: " % (num1))
suma = sum(range(num1, num2+1))
if num2<=num1:
    print "No has introducido un numero mayor que el primero"

else:

    for i in range (num1, num2):
        print i,'+',
    print i+1,'=',suma
