from tkinter import Tk, Label, Entry, Button, Checkbutton, StringVar, OptionMenu
from PIL import Image, ImageDraw, ImageFont
from tkcalendar import DateEntry
import re
from datetime import datetime, timedelta
import tkinter as tk
from funciones import *
dibujo = None
def generar_asignacion():
    global ingresar_semana_date, nombre_entry, ayudante_entry, contador_imagenes, dibujo
    try:
        mensaje_completado.config(text="")
        texto_actividad = opcion_seleccionada.get().lower()
        texto_nombre = nombre_entry.get()
        texto_ayudante = ayudante_entry.get().capitalize()

        if contador_imagenes == 4:
            # Sumar una semana a la fecha almacenada en ingresar_semana
            fecha_dada = datetime.strptime(ingresar_semana_date.get(), "%d-%m-%Y")
            fecha_dada += timedelta(weeks=1)
            ingresar_semana_date.set(fecha_dada.strftime("%d-%m-%Y"))
            mensaje_completado.config(text=f'Asignaciones Completadas para la semana: {fecha_dada.strftime("%d-%m-%Y")}')
            contador_imagenes = 0
        
        contador_imagenes += 1

        # Cargar la imagen original en cada iteración
        imagen = Image.open("image/Asignaciones.jpg")
        imagen = imagen.convert("RGB")
        dibujo = ImageDraw.Draw(imagen)
        fuente = ImageFont.truetype("fonts/Calibri.ttf", 26)

        # Agregar Semana a la Imagen 
        dibujo.text((112,190), ingresar_semana_date.get(), fill=(0, 0, 0), font=fuente)
       
        # Reemplazar caracteres no válidos en el nombre de archivo
        nombre_archivo = re.sub(r"[^\w\s-]", "", texto_nombre.strip())
        nombre_archivo = re.sub(r"[\s]+", "_", nombre_archivo)

        # Generar el nombre de archivo único basado en el texto
        nombre_archivo = nombre_archivo + ".jpg"

        #Definimos Actividad
        asignacion_actividad(texto_actividad,dibujo, texto_nombre, texto_ayudante, fuente)
        #Definimos Sala
        asignacion_sala(opcion_principal,opcion_auxiliar,dibujo)
        #Guardamos Imagen
        guardar_imagen(imagen, nombre_archivo, texto_nombre)
        
        #Mensaje de Asignacion descargada
        mensaje_completado_nombre.config(text=guardar_imagen(imagen, nombre_archivo, texto_nombre))

        #Variables Vacias 
        nombre_entry.set("")
        ayudante_entry.set("")
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

# Variables para almacenar los datos ingresados por el usuario
ingresar_semana_date = StringVar()
nombre_entry = StringVar()
ayudante_entry = StringVar()
contador_imagenes = 0

#Opciones Asignaciones
opciones_asignaciones = ['Seleccionar Asignacion', 'Lectura','Primera Conversacion', 'Revisita', 'Curso Biblico', 'Discurso', 'Otro']
opcion_seleccionada = StringVar()
opcion_seleccionada.set(opciones_asignaciones[0])


#Mensaje Semana Completada
mensaje_completado = Label(ventana, text="", fg="green")
mensaje_completado.pack()

# Entrada para la fecha
Label(ventana, text="Seleccionar fecha:", font=fuente_opciones).pack()
DateEntry(ventana, textvariable=ingresar_semana_date, date_pattern='dd-mm-yyyy', font=fuentes_seleccionables).pack()
Label(ventana, text='').pack()

#Entrada para la actividad
Label(ventana, text='Ingrese la Actividad: ',font=fuente_opciones).pack()
OptionMenu(ventana, opcion_seleccionada, *opciones_asignaciones).pack()
Label(ventana, text='').pack()

#Entrada Nombre
Label(ventana, text="Nombre:", font=fuente_opciones).pack()
Entry(ventana, textvariable=nombre_entry).pack()
Label(ventana, text='').pack()

#Entrada Ayudante
Label(ventana, text="Ayudante:", font=fuente_opciones).pack()
Entry(ventana, textvariable=ayudante_entry).pack()
Label(ventana, text='').pack()

#Opciones Salas
opcion_principal = tk.BooleanVar()
opcion_auxiliar = tk.BooleanVar()
opcion_sala_principal = Checkbutton(ventana, text='Sala Principal', variable=opcion_principal, command= asignacion_sala, font=fuente_opciones)
opcion_sala_principal.pack()
opcion_sala_auxiliar = Checkbutton(ventana, text='Sala Auxiliar',variable=opcion_auxiliar, command=asignacion_sala, font=fuente_opciones)
opcion_sala_auxiliar.pack()
Label(ventana, text='').pack()

# Botón para generar la asignación
Button(ventana, text="Generar Asignación", command=generar_asignacion).pack()

#Mensaje de Asiganacion Descargada
mensaje_completado_nombre = Label(ventana, text='', fg='green')
mensaje_completado_nombre.pack()
Label(ventana, text='').pack()

# Enlace del evento de presionar Enter a la función de generar asignación
ventana.bind('<Return>', activar_generar_asignacion)

# Etiqueta para mostrar el mensaje de error
mensaje_error = Label(ventana, text="", fg="red")
mensaje_error.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()





