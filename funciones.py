from tkinter import Tk, Label, Entry, Button, Checkbutton, StringVar, OptionMenu
from PIL import Image, ImageDraw, ImageFont
from tkcalendar import DateEntry
import re
from datetime import datetime, timedelta
import tkinter as tk
import os
dibujo = None

def guardar_imagen(imagen, texto_nombre):

    # Reemplazar caracteres no válidos en el nombre de archivo
    nombre_archivo = re.sub(r"[^\w\s-]", "", texto_nombre.strip())
    nombre_archivo = re.sub(r"[\s]+", "_", nombre_archivo)

    # Generar el nombre de archivo único basado en el texto
    nombre_archivo = nombre_archivo + ".jpg"
    ruta_escritorio = os.path.expanduser('~/Desktop')
    carpeta_asignaciones = os.path.join(ruta_escritorio, 'Asignaciones')
    if not os.path.exists(carpeta_asignaciones):
        os.mkdir(carpeta_asignaciones)
    ruta_archivo = os.path.join(carpeta_asignaciones, nombre_archivo)
    imagen.save(ruta_archivo)
    msj = f'Asignacion de {texto_nombre} descargada'
    return(msj)

def asignacion_actividad(texto_actividad, dibujo, texto_nombre, texto_ayudante, fuente, aclaraciones_entry, fuente_aclaraciones):
        
        ban = 0
        if texto_actividad == "lectura":
            dibujo.rectangle([(53, 298), (65, 309)], fill="#946FBD", width=2)
            ban = 0
        elif texto_actividad == "primera conversacion":
            dibujo.rectangle([(53, 320), (65, 331)], fill="#946FBD", width=2)
            dibujo.text((85,338), aclaraciones_entry, fill=(0, 0, 0), font=fuente_aclaraciones)
            ban = 1
        elif texto_actividad == "revisita":
            dibujo.rectangle([(53, 365), (65, 376)], fill="#946FBD", width=2)
            dibujo.text((85,380), aclaraciones_entry, fill=(0, 0, 0), font=fuente_aclaraciones)
            ban = 1
        elif texto_actividad == "curso biblico":
            dibujo.rectangle([(305, 298), (317, 309)], fill="#946FBD", width=2)
            ban = 1 
        elif texto_actividad == "discurso":
            dibujo.rectangle([(305, 320), (317, 331)], fill="#946FBD", width=2)
            ban = 0
        else:
            dibujo.rectangle([(305, 343),(317, 354)], fill='#946FBD', width=2)
            dibujo.text((383,338), aclaraciones_entry, fill=(0, 0, 0), font=fuente_aclaraciones)
            ban = 1

        if ban == 0:
            dibujo.text((136, 93), (texto_nombre), fill=(0, 0, 0), font=fuente)
        elif ban == 1:
            dibujo.text((136, 93), (texto_nombre), fill=(0, 0, 0), font=fuente)
            dibujo.text((155, 142), (texto_ayudante), fill=(0, 0, 0), font=fuente)
            
def asignacion_sala(a,b,dibujo):
    if a.get():
        dibujo.rectangle([(53, 450), (65, 461)], fill="#946FBD", width=2)
    elif b.get():
        dibujo.rectangle([(53, 473),(65, 484)],fill="#946FBD",width=2)

