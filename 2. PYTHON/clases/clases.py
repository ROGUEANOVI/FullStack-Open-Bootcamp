# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ovidio Antonio Romero Guerrero
# Created Date: 2002/07/25
# version ='1.0'
# ---------------------------------------------------------------------------
""" Programa para crear clases e instanciarlas"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------


class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self._color = color
        self._ruedas = ruedas
        self._puertas = puertas

    _color = ""
    _ruedas = 0
    _puertas = 0

    def setcolor(self, color):
        self._color = color

    def setruedas(self, ruedas):
        self._ruedas = ruedas

    def setpuertas(self, puertas):
        self._puertas = puertas

    def getcolor(self):
        return self._color

    def getruedas(self):
        return self._ruedas

    def getpuertas(self):
        return self._puertas


class Coche(Vehiculo):

    def __init__(self, velocidad, cilindrada):
        super(Vehiculo, self).__init__()
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    _velocidad = 0
    _cilindrada = ""

    def setvelocidad(self, velocidad):
        self._velocidad = velocidad

    def setcilindrada(self, cilindrada):
        self._cilindrada = cilindrada

    def getvelocidad(self):
        return self._velocidad

    def getcilindrada(self):
        return self._cilindrada


micoche = Coche(80, "1000 c.c")

micoche.setcolor("Rojo")
micoche.setruedas(4)
micoche.setpuertas(5)


print(micoche.getcolor())
print(micoche.getruedas())
print(micoche.getpuertas())
