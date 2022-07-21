# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ovidio Antonio Romero Guerrero
# Created Date: 2002/07/20
# version ='1.0'
# ---------------------------------------------------------------------------
""" Program que valida la mayoria de edad de un usuario """
# ---------------------------------------------------------------------------
# Imports 
# ---------------------------------------------------------------------------
edad=int(input("Ingrese la edad: "))

if edad > 0 and edad <= 150:
    if edad >= 18:
        print("Es mayor de edad.")
    else:
        print("Es menor de edad.")
else:
    print("Edad invalida. Ingrese una edad razonable entre 1 y 150  años")
