# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ovidio Antonio Romero Guerrero
# Created Date: 2002/07/25
# version ='1.0'
# ---------------------------------------------------------------------------
""" Programa que clcula el area de un triangulo y un circulo mediante funciones"""
# ---------------------------------------------------------------------------
# Imports
import math


# ---------------------------------------------------------------------------

def calcular_area_triangulo(base: float, altura: float) -> float:
    area = (base * altura) / 2
    return area


areaTriangulo = calcular_area_triangulo(2, 20)
print(areaTriangulo)


def calcular_area_circulo(radio: float) -> float:
    area = math.pi * radio ** 2
    return area


areaCirculo = calcular_area_circulo(2)
print(areaCirculo)
