# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ovidio Antonio Romero Guerrero
# Created Date: 2002/07/25
# version ='1.0'
# ---------------------------------------------------------------------------
""" Programa que muestra si es la hora de salida y si no calcula cuanto hace falta para la salida """
# ---------------------------------------------------------------------------
# Imports
from datetime import datetime
# ---------------------------------------------------------------------------

hora_acutal = datetime.today().hour

if hora_acutal == 19:
    print(f"Son las {hora_acutal} es hora de SALIDA")
elif hora_acutal < 19:
    horasRestantes = 19 - datetime.today().hour
    print(f"Son las {hora_acutal}  te quedan {horasRestantes} horas de TRABAJO")
