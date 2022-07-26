# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ovidio Antonio Romero Guerrero
# Created Date: 2002/07/25
# version ='1.0'
# ---------------------------------------------------------------------------
""" Proyecto con modulos main, operaciones """
# ---------------------------------------------------------------------------
# Imports
import operaciones as op
# ---------------------------------------------------------------------------


def main():
    suma = op.sumar(10, 5)
    resta = op.restar(10, 5)
    multiplicacion = op.multiplicar(10, 5)
    division = op.dividir(10, 5)

    print(suma)
    print(resta)
    print(multiplicacion)
    print(division)


if __name__ == "__main__":
    main()
