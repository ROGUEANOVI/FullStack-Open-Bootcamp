# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ovidio Antonio Romero Guerrero
# Created Date: 2002/07/25
# version ='1.0'
# ---------------------------------------------------------------------------
""" Programa para crea un archivo .txt"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

archivo = open("E:/Documentos/4. CURSOS PROGRAMACION/5. OPEN BOOTCAMP/2. PYTHON/crear_archivo_txt/archivo.txt", "w")
archivo.write("Primera linea del archivo\n")
archivo.write("Segunda linea del archivo\n")
archivo.close()
