from tkinter import Tk, Label, Entry, Button, Checkbutton, StringVar, OptionMenu
from PIL import Image, ImageDraw, ImageFont
from tkcalendar import DateEntry
import re
from datetime import datetime, timedelta
import tkinter as tk
from funciones import *
import locale
locale.setlocale(locale.LC_TIME, "es_ES.utf8")
dibujo = None


def generar_asignacion():
    global ingresar_semana_date, nombre_entry, ayudante_entry, dibujo, aclaraciones_entry
    try:
        texto_actividad = opcion_seleccionada.get().lower()
        texto_nombre = nombre_entry.get()
        texto_ayudante = ayudante_entry.get().capitalize()
        aclaraciones = aclaraciones_entry.get()

        # Cargar la imagen original en cada iteración
        imagen = Image.open("image/Asignaciones.jpg")
        imagen = imagen.convert("RGB")
        dibujo = ImageDraw.Draw(imagen)
        fuente = ImageFont.truetype("fonts/Calibri.ttf", 26)
        fuente_aclaraciones = ImageFont.truetype("fonts/Calibri.ttf", 18)
        # Agregar Semana a la Imagen 
        dibujo.text((112,190), ingresar_semana_date.get(), fill=(0, 0, 0), font=fuente)

        #Definimos Actividad
        asignacion_actividad(texto_actividad,dibujo, texto_nombre, texto_ayudante, fuente, aclaraciones, fuente_aclaraciones)

        #Definimos Sala
        asignacion_sala(opcion_principal,opcion_auxiliar,dibujo)

        #Guardamos Imagen
        guardar_imagen(imagen, texto_nombre)
        
        #Mensaje de Asignacion descargada
        mensaje_completado_nombre.config(text=guardar_imagen(imagen, texto_nombre))

        #Variables Vacias 
        nombre_entry.set("")
        ayudante_entry.set("")
        aclaraciones_entry.set("")
        mensaje_error.config(text="")
      
    except Exception as e:
        mensaje_error.config(text=f"Ocurrió un error al generar la asignación {e}")

# Función para activar el botón "Generar Asignación" al presionar Enter
def activar_generar_asignacion(event):
    generar_asignacion()

#-------------------------------------------- TKINTER -------------------------------------------------

# Crear la ventana principal
ventana = Tk()
ventana.title("Generador de Asignaciones")
ventana.geometry('400x500')
fuente_opciones = ('Calibri', 22)
fuentes_seleccionables = ('Calibri', 18)
icon_path = "image/logo.ico"  
ventana.iconbitmap(icon_path)

# Variables para almacenar los datos ingresados por el usuario
ingresar_semana_date = StringVar()
nombre_entry = StringVar()
ayudante_entry = StringVar()
opcion_seleccionada = StringVar()
aclaraciones_entry = StringVar()

# Entrada para la fecha
Label(ventana, text='Seleccionar fecha:', font=fuente_opciones).pack()
DateEntry(ventana, textvariable=ingresar_semana_date, date_pattern='dd-mm-yyyy', font=fuentes_seleccionables, locale="es_ES").pack()

#Entrada para la actividad
Label(ventana, text='Ingrese la Actividad: ',font=fuente_opciones).pack()
opciones_asignaciones = ['Seleccionar Asignacion', 'Lectura','Primera Conversacion', 'Revisita', 'Curso Biblico', 'Discurso', 'Otro']
opcion_seleccionada.set(opciones_asignaciones[0])
OptionMenu(ventana, opcion_seleccionada, *opciones_asignaciones).pack()

#Entrada Nombre
Label(ventana, text="Nombre:", font=fuente_opciones).pack()
Entry(ventana, textvariable=nombre_entry).pack()

#Entrada Ayudante
Label(ventana, text='Ayudante:', font=fuente_opciones).pack()
Entry(ventana, textvariable=ayudante_entry).pack()

#Entrada Aclaraciones
Label(ventana, text='Aclaraciones: ', font=fuente_opciones).pack()
Entry(ventana, textvariable=aclaraciones_entry).pack()

#Opciones Salas
opcion_principal = tk.BooleanVar()
opcion_auxiliar = tk.BooleanVar()
opcion_sala_principal = Checkbutton(ventana, text='Sala Principal', variable=opcion_principal, command= asignacion_sala, font=fuente_opciones).pack()
opcion_sala_auxiliar = Checkbutton(ventana, text='Sala Auxiliar',variable=opcion_auxiliar, command=asignacion_sala, font=fuente_opciones).pack()

# Botón para generar la asignación
Button(ventana, text="Generar Asignación", command=generar_asignacion).pack()

#Mensaje de Asiganacion Descargada
mensaje_completado_nombre = Label(ventana, text='', fg='green')
mensaje_completado_nombre.pack()

# Enlace del evento de presionar Enter a la función de generar asignación
ventana.bind('<Return>', activar_generar_asignacion)

# Etiqueta para mostrar el mensaje de error
mensaje_error = Label(ventana, text="", fg="red")
mensaje_error.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()





