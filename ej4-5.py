# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA4 - EJERCICIO 5
Escriu un programa que demani l'amplada i alçada d'un rectangle i ho dibuixi de
 la següent manera:
*****
*****
*****

 """

altura= int(input("Escriba la altura del rectangulo:"))
ancho= int(input("Escriba la anchura del rectangulo:"))

for i in range(altura):

    for l in range(ancho):
        print "*",
    print ""
