# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA4 - EJERCICIO 4
Escriu un programa que demani un nombre i calculi el seu factorial."""

print"EL FACTORIAL DE UN NUMERO"
num=int(input("Escribe un numero:"))
factorial = 1
for posicion in range (1, (num+1)):
        factorial = factorial * posicion
print "El factorial del numero es: %d" % (factorial)
