# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ovidio Antonio Romero Guerrero
# Created Date: 2002/07/25
# version ='1.0'
# ---------------------------------------------------------------------------
""" Programa que muestra si un año es bisiesto o no, mediante una funcion"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------


def es_bisiesto(anio):
    if ((anio % 4) == 0) and ((anio % 100) != 0 or (anio % 400) == 0):
        return f"{anio} es bisiesto"
    else:
        return f"{anio} NO es bisiesto"


bisiesto = es_bisiesto(2015)
print(bisiesto)
