#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Ovidio Antonio Romero Guerrero
# Created Date: 2002/07/21
# version ='1.0'
# ---------------------------------------------------------------------------
""" Programa que calcula muestra los numeros impares en un rango de numeros"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
numero_inicial = int(input("Ingrese el numero inicial: "))
numero_final = int(input("Ingrese el numero final: "))
lista_impares = []
while(numero_final <= numero_inicial):
  numero_final = int(input("El numero_final debe ser mayor al numero inicial por favor, introduce otro numero: "))

for numero in range(numero_inicial,numero_final + 1):
  if ((numero % 2) != 0):
    lista_impares.append(numero)

print(lista_impares)



