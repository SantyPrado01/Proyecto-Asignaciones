from tkinter import Tk, Label, Entry, Button, Checkbutton, StringVar, OptionMenu
from PIL import Image, ImageDraw, ImageFont
from tkcalendar import DateEntry
import re
import tkinter as tk
from funciones import *



dibujo = None
    
def generar_asignacion():
    global ingresar_semana_date, nombre_entry, ayudante_entry, dibujo, opcion_principal, opcion_auxiliar, opcion_seleccionada_intervencion, opcion_seleccionada_numeros

    numero_intervencion = opcion_seleccionada_numeros.get()
    intervencion = opcion_seleccionada_intervencion.get()  
    nombre = nombre_entry.get()
    ayudante = ayudante_entry.get()
    fecha = ingresar_semana_date.get()
    sala_a = opcion_principal.get()
    sala_b = opcion_auxiliar.get()


    # Cargar la imagen original en cada iteración
    imagen = Image.open("image/Asignaciones.png")
    imagen = imagen.convert("RGB")
    dibujo = ImageDraw.Draw(imagen)
    fuente = ImageFont.truetype("fonts/Calibri.ttf", 26)
    
    # Agregar Semana a la Imagen 
    dibujo.text((319,600), fecha, fill=(0, 0, 0), font=fuente)

    #Definimos Actividad
    asignacion_actividad(intervencion, numero_intervencion, dibujo, nombre, ayudante, fuente)

    #Definimos Sala
    asignacion_sala(sala_a, sala_b, dibujo)

    #Guardamos Imagen
    guardar_imagen(imagen, nombre)


    #Variables Vacias 
    nombre_entry.delete(0, 'end')
    ayudante_entry.delete(0, 'end')
    
    

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
icon_path = "image/Logo.ico"  
ventana.iconbitmap(icon_path)

# Variables para almacenar los datos ingresados por el usuario
ingresar_semana_date = StringVar()
nombre_entry = StringVar()
ayudante_entry = StringVar()
opcion_seleccionada_numeros = StringVar()
opcion_seleccionada_intervencion = StringVar()
aclaraciones_entry = StringVar()

# Entrada para la fecha
label_fecha = Label(ventana, text='Seleccionar fecha:', font=fuente_opciones)
label_fecha.pack()

entry_fecha = DateEntry(ventana, textvariable=ingresar_semana_date, date_pattern='dd-mm-yyyy', font=fuentes_seleccionables, locale="es_ES")
entry_fecha.pack()

#Entrada para la actividad
opciones_asignaciones_numeros = ['Intervencion Numero', '3.','4.','5.','6.','7.','8.','9.','10.']
opcion_seleccionada_numeros.set(opciones_asignaciones_numeros[0])
option_menu_numeros = ttk.OptionMenu(ventana, opcion_seleccionada_numeros, *opciones_asignaciones_numeros)
option_menu_numeros.pack()

opciones_intervenciones = ['Intervencion','Lectura','Empiece conversaciones','Haga revisitas','Haga Discípulos','Explique sus Creencias','Discurso']
opcion_seleccionada_intervencion.set(opciones_intervenciones[0])
option_menu_intervenciones = ttk.OptionMenu(ventana, opcion_seleccionada_intervencion, *opciones_intervenciones)
option_menu_intervenciones.pack()

#Entrada Nombre
nombre_label = Label(ventana, text="Nombre:", font=fuente_opciones)
nombre_label.pack()

nombre_entry = ttk.Entry(ventana, textvariable=nombre_entry)
nombre_entry.pack()

#Entrada Ayudante
ayudante_label = Label(ventana, text='Ayudante:', font=fuente_opciones)
ayudante_label.pack()

ayudante_entry = ttk.Entry(ventana, textvariable=ayudante_entry)
ayudante_entry.pack()

#Opciones Salas
opcion_principal = tk.BooleanVar()
opcion_auxiliar = tk.BooleanVar()

opcion_sala_principal = ttk.Checkbutton(ventana, text='Sala Principal', variable=opcion_principal)
opcion_sala_principal.pack()

opcion_sala_auxiliar = ttk.Checkbutton(ventana, text='Sala Auxiliar',variable=opcion_auxiliar)
opcion_sala_auxiliar.pack()

# Botón para generar la asignación
boton_guardar = ttk.Button(ventana, text="Guardar Asignación", command=generar_asignacion)
boton_guardar.pack()

# Enlace del evento de presionar Enter a la función de generar asignación
ventana.bind('<Return>', activar_generar_asignacion)

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()





