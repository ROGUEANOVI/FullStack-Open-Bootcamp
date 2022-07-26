
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ovidio Antonio Romero Guerrero
# Created Date: 2002/07/25
# version ='1.0'
# ---------------------------------------------------------------------------
""" Programa para crear la clase alumno con sus diferentes metodos"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------


class Alumno:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    _nombre = ""
    _nota = 0.0

    def setnombre(self, nombre):
        self._nombre = nombre

    def setnota(self, nota):
        self._nota = nota

    def getnombre(self):
        return self._nombre

    def getnota(self):
        return self._nota


alumno1 = Alumno("Ovidio", 4.9)

alumno1.setnombre("Ovidio Romero")
alumno1.setnota(6.0)

nombreAlumno = alumno1.getnombre()
notaAlumno = alumno1.getnota()

if notaAlumno >= 3.5 and notaAlumno <= 5:
    print(f"El alumno {nombreAlumno} con nota {notaAlumno} es APROBADO")
elif notaAlumno < 3.5 and notaAlumno >= 0:
    print(f"El alumno {nombreAlumno} con nota {notaAlumno} fue REPROBADO")
else:
    print("La nota es invalida")
