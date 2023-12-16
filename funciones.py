from tkinter import messagebox, Button
from PIL import Image, ImageDraw, ImageFont
from tkcalendar import DateEntry
import re
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
import os
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.lib import pdfencrypt
from reportlab.pdfgen import canvas
import subprocess

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
    messagebox.showinfo('Completado', f'Asigancion {nombre_archivo} descargada.')

def asignacion_actividad(texto_actividad, numero_intervencion, dibujo, texto_nombre, texto_ayudante, fuente):
        
        ban = 0
        texto = numero_intervencion + texto_actividad 
        fuente_chica = ImageFont.truetype("fonts/Calibri.ttf", 60)
        if texto_actividad == "Lectura":
            dibujo.text((732,685),texto, fill=(0,0,0), font=fuente)
            ban = 0
        elif texto_actividad == "Empiece conversaciones":
            dibujo.text((732,697), texto, fill=(0, 0, 0), font=fuente_chica)
            ban = 1
        elif texto_actividad == "Haga revisitas":
            dibujo.text((732,685), texto, fill=(0, 0, 0), font=fuente)
            ban = 1
        elif texto_actividad == "Haga Discípulos":
            dibujo.text((732,685), texto, fill=(0, 0, 0), font=fuente)
            ban = 1 
        elif texto_actividad == 'Explique sus Creencias':
            dibujo.text((732,697), texto, fill=(0, 0, 0), font=fuente_chica)
            ban = 0
        elif texto_actividad == "Discurso":
            dibujo.text((732,685), texto, fill=(0, 0, 0), font=fuente)
            ban = 0

        if ban == 0:
            dibujo.text((388, 272), (texto_nombre), fill=(0, 0, 0), font=fuente)
        elif ban == 1:
            dibujo.text((388, 272), (texto_nombre), fill=(0, 0, 0), font=fuente)
            dibujo.text((438, 412), (texto_ayudante), fill=(0, 0, 0), font=fuente)
            
def asignacion_sala(sala_a,sala_b,dibujo):
    if sala_a:
        dibujo.rectangle([(157, 1017), (202, 1063)], fill="#946FBD", width=2)
    elif sala_b:
        dibujo.rectangle([(157, 1102),(202, 1149)],fill="#946FBD",width=2)



