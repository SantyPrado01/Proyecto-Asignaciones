from tkinter import messagebox, Button
from PIL import Image, ImageDraw, ImageFont
from tkcalendar import DateEntry
import re
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
import os
from comandosSql import *
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.lib import pdfencrypt
from reportlab.pdfgen import canvas


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
        if texto_actividad == "Lectura":
            dibujo.rectangle([(53, 298), (65, 309)], fill="#946FBD", width=2)
            ban = 0
        elif texto_actividad == "Primera Conversacion":
            dibujo.rectangle([(53, 320), (65, 331)], fill="#946FBD", width=2)
            dibujo.text((85,338), aclaraciones_entry, fill=(0, 0, 0), font=fuente_aclaraciones)
            ban = 1
        elif texto_actividad == "Revisita":
            dibujo.rectangle([(53, 365), (65, 376)], fill="#946FBD", width=2)
            dibujo.text((85,380), aclaraciones_entry, fill=(0, 0, 0), font=fuente_aclaraciones)
            ban = 1
        elif texto_actividad == "Curso Biblico":
            dibujo.rectangle([(305, 298), (317, 309)], fill="#946FBD", width=2)
            ban = 1 
        elif texto_actividad == "Discurso":
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
            
def asignacion_sala(sala_a,sala_b,dibujo):
    if sala_a:
        dibujo.rectangle([(53, 450), (65, 461)], fill="#946FBD", width=2)
    elif sala_b:
        dibujo.rectangle([(53, 473),(65, 484)],fill="#946FBD",width=2)

def insertar_asignacion(asignacion):
    base_datos = sqlite3.connect('hermanos.bd')
    cursor = base_datos.cursor()
    cursor.execute("INSERT OR IGNORE INTO asignacion (nombre) VALUES (?)", (asignacion,))
    base_datos.commit()

def insertar_fecha(fecha):
    base_datos = sqlite3.connect('hermanos.bd')
    cursor = base_datos.cursor()
    cursor.execute("INSERT OR IGNORE INTO fecha (fecha) VALUES (?)", (fecha,))
    base_datos.commit()

def insertar_sala (sala):
    base_datos = sqlite3.connect('hermanos.bd')
    cursor = base_datos.cursor()
    cursor.execute("INSERT OR IGNORE INTO salas (nombre) VALUES (?)", (sala,))
    base_datos.commit()

def insertar_ayudante(ayudante):
    base_datos = sqlite3.connect('hermanos.bd')
    cursor = base_datos.cursor()
    cursor.execute("INSERT OR IGNORE INTO ayudante (nombre) VALUES (?)", (ayudante,))
    base_datos.commit()

def guardar_asignacion(nombre, ayudante, asignacion, fecha, sala):
    
    insertar_asignacion(asignacion)
    insertar_ayudante(ayudante)
    insertar_fecha(fecha)
    insertar_sala(sala)

    base_datos = sqlite3.connect('hermanos.bd')
    cursor = base_datos.cursor()
    # Obtiene los IDs de marca y categoría
    cursor.execute("SELECT ayudante_id FROM ayudante WHERE nombre = ?", (ayudante,))
    ayudante_id = cursor.fetchone()

    cursor.execute("SELECT asignacion_id FROM asignacion WHERE nombre = ?", (asignacion,))
    asignacion_id = cursor.fetchone()

    cursor.execute("SELECT fecha_id FROM fecha WHERE fecha = ?", (fecha,))
    fecha_id = cursor.fetchone()

    cursor.execute("SELECT sala_id FROM salas WHERE nombre = ?", (sala,))
    sala_id = cursor.fetchone()
    
    cursor.execute("INSERT INTO hermanos (nombre, ayudante_id, asignacion_id, fecha_id, sala_id) VALUES (?, ?, ?, ?, ?)",
                   (nombre, ayudante_id[0], asignacion_id[0], fecha_id[0], sala_id[0]))

    base_datos.commit()      

base_datos.close()

def descargar_pdf(treeview, filename, nombre_a_indice):

    ruta_escritorio = os.path.expanduser('~/Desktop')
    carpeta_asignaciones = os.path.join(ruta_escritorio, 'Asignaciones')
    if not os.path.exists(carpeta_asignaciones):
        os.mkdir(carpeta_asignaciones)
    ruta_archivo = os.path.join(carpeta_asignaciones, filename)

    archivo = canvas.Canvas(ruta_archivo, pagesize=letter)

    # Configurar los márgenes, fuentes y colores
    left_margin = 10
    right_margin = 10
    top_margin = 35
    bottom_margin = 10

    width, height = letter
    archivo.setPageSize((width, height))
    archivo.setFont("Helvetica", 12)

    # Configurar el encabezado del PDF
    columnas = list(nombre_a_indice.keys())
    x = left_margin
    y = height - top_margin
    espacio_entre_lineas = 15  # Espacio vertical entre líneas

    for col in columnas:
        encabezado = treeview.heading(col, "text")
        x_centered = x + (100 - archivo.stringWidth(encabezado, "Helvetica", 12)) / 2
        archivo.drawString(x_centered, y, encabezado)
        x += 125  # Espacio horizontal entre columnas

    # Obtener los datos del Treeview
    filas = treeview.get_children()
    y -= espacio_entre_lineas  # Mover hacia abajo para los datos

    for fila in filas:
        x = left_margin
        datos = [treeview.item(fila, 'values')[nombre_a_indice[col]] for col in columnas]

        # Obtener el estilo de fondo de la fila
        fecha_estilo = fecha_color(datos[3])  # Suponemos que la fecha está en la quinta columna

        for i, dato in enumerate(datos, start=1):
            # Configurar el color de fondo según la fecha
            if fecha_estilo == "FechaVerde":
                archivo.setFillColorRGB(160 / 255, 255 / 255, 143 / 255)  # Verde
            elif fecha_estilo == "FechaRoja":
                archivo.setFillColorRGB(255 / 255, 143 / 255, 146 / 255)  # Rojo
            else:
                archivo.setFillColorRGB(1, 1, 1)  # Blanco (predeterminado)

            width = 100  # Ancho de la celda
            height = espacio_entre_lineas  # Altura de la celda
            text_width = archivo.stringWidth(str(dato), "Helvetica", 12)
            x_centered = x + (width - text_width) / 2

            archivo.rect(x, y, width, -height, fill=True, stroke=False)
            archivo.setFillColorRGB(0, 0, 0)  # Color de texto negro
            archivo.drawString(x_centered, y - 10, str(dato))
            x += 125  # Espacio horizontal entre columnas

        y -= espacio_entre_lineas  # Mover hacia abajo para la siguiente fila
    archivo.showPage()  # Mostrar la página actual
    archivo.save()

def fecha_color(fecha_str):
    fecha = datetime.strptime(fecha_str, "%d-%m-%Y")
    dos_meses_atras = datetime.now() - timedelta(days=60)
    
    if fecha < dos_meses_atras:
        return "FechaVerde"
    else:
        return "FechaRoja"

def buscar_todos():
    base_datos = sqlite3.connect('hermanos.bd')
    cursor = base_datos.cursor()
    
    cursor.execute('SELECT * FROM hermanos')
    hermanos = cursor.fetchall()
    
    if not hermanos:
        messagebox.showerror('Error', f'No Encontrado')
    else:
        ventana_emergente_2 = tk.Toplevel()
        tree = ttk.Treeview(ventana_emergente_2, columns=('Nombre', 'Ayudante', 'Asignacion', 'Fecha', 'Sala'))
        
        tree.column("#0", width =0, stretch=tk.NO)
        tree.heading("#1", text="Nombre", anchor=tk.CENTER)
        tree.heading("#2", text="Ayudante", anchor=tk.CENTER)
        tree.heading("#3", text="Asignacion", anchor=tk.CENTER)
        tree.heading("#4", text="Fecha", anchor=tk.CENTER)
        tree.heading("#5", text="Sala", anchor=tk.CENTER)
        
        for i in range(1, 6):
            tree.column(f"#{i}", anchor=tk.CENTER)
        
        style = ttk.Style()
        style.configure("FechaVerde.Treeview", background="green")
        style.configure("FechaRoja.Treeview", background="red")
        
        for tema in hermanos:
            id, nombre, ayudante_id, asignacion_id, fecha_id, sala_id = tema
            
            cursor.execute("SELECT nombre FROM ayudante WHERE ayudante_id=?", (ayudante_id,))
            ayudante_nombre = cursor.fetchone()[0]
            
            cursor.execute("SELECT nombre FROM asignacion WHERE asignacion_id=?", (asignacion_id,))
            asignacion_nombre = cursor.fetchone()[0]
            
            cursor.execute("SELECT fecha FROM fecha WHERE fecha_id=?", (fecha_id,))
            fecha_dato = cursor.fetchone()[0]
            
            cursor.execute("SELECT nombre FROM salas WHERE sala_id=?", (sala_id,))
            sala_nombre = cursor.fetchone()[0]
            
            fecha_estilo = fecha_color(fecha_dato)
            
            tree.insert('', 'end', values=[nombre, ayudante_nombre, asignacion_nombre, fecha_dato, sala_nombre], tags=(fecha_estilo,))
        
        tree.tag_configure("FechaVerde", background="#A0FF8F")
        tree.tag_configure("FechaRoja", background="#FF8F92")

        tree.grid(row=0, column=0, padx=10, pady=10)
        nombre_pdf = 'Asignaciones.pdf'

        nombre_a_indice = {'#1':0,'#2': 1, '#3': 2, '#4': 3, '#5': 4}
        # Para cada columna, elimina el '#' si está presente
        boton_descargar_pdf = Button(ventana_emergente_2, text='Descargar PDF', command=lambda:descargar_pdf(tree, nombre_pdf, nombre_a_indice))
        boton_descargar_pdf.grid(row=1, column=0)
    
    base_datos.close()


