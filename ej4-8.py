# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA4 - EJERCICIO 8
Escriu un programa que demani l'amplada d'un triangle i ho dibuixi de la següent manera:

Alçada del triangle: 4
*
**
***
****
***
**
*

"""
altura= int(input("Escriba la altura del rectangulo:"))
anchura= altura

for i in range (anchura):
    print "*"*i
for i in range(altura):
    print "*"*(altura)
    altura=altura-1
