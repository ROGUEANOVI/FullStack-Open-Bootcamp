# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ovidio Antonio Romero Guerrero
# Created Date: 2002/07/25
# version ='1.0'
# ---------------------------------------------------------------------------
""" Programa que muestra si un numero es primo o no por medio de una funcion"""
# ---------------------------------------------------------------------------
# Imports

# ---------------------------------------------------------------------------


def es_primo(numero: int) -> bool:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(f"No es primo. El {numero} es divisible  por {i}")
            return False
    print("Es primo")
    return True


es_primo(20)
