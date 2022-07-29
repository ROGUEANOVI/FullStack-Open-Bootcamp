# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ovidio Antonio Romero Guerrero
# Created Date: 2002/07/28
# version ='1.0'
# ---------------------------------------------------------------------------
""" Programa para crear un archivo .txt"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

archivo = open("E:/Documentos/4. CURSOS PROGRAMACION/5. OPEN BOOTCAMP/2. PYTHON/crear_archivo_txt/archivo.txt", "w")
archivo.write("Primera linea del archivo\n")
archivo.close()

archivo = open("archivo.txt", "r+")
archivo.readline()
archivo.write('Esta es la segunda vez que escribo.\n')
archivo.close()
