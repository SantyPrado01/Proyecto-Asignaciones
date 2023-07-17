import os
def nombre_mayuscula(a):
    palabras = a.split()
    nombre = palabras[0].capitalize()
    apellido = palabras[-1].capitalize()
    nombre_mayus = nombre + ' '.join(palabras[1:-1]) + " " + apellido
    return (nombre_mayus)

def guardar_imagen(imagen, nombre_archivo, texto_nombre):
    ruta_escritorio = os.path.expanduser('~/Desktop')
    carpeta_asignaciones = os.path.join(ruta_escritorio, 'Asignaciones')
    if not os.path.exists(carpeta_asignaciones):
        os.mkdir(carpeta_asignaciones)
    ruta_archivo = os.path.join(carpeta_asignaciones, nombre_archivo)
    imagen.save(ruta_archivo)
    msj = f'Asignacion de {nombre_mayuscula(texto_nombre)} descargada'
    return(msj)

def asignacion_actividad(texto_actividad, dibujo, texto_nombre, texto_ayudante, fuente):
        ban = 0
        if texto_actividad == "lectura":
            dibujo.rectangle([(94, 464), (113, 495)], fill="blue", width=2)
            ban = 0
        elif texto_actividad == "primera conversacion":
            dibujo.rectangle([(95, 504), (116, 534)], fill="blue", width=2)
            ban = 1
        elif texto_actividad == "revisita":
            dibujo.rectangle([(95, 583), (113, 613)], fill="blue", width=2)
            ban = 1
        elif texto_actividad == "curso biblico":
            dibujo.rectangle([(387, 465), (405, 495)], fill="blue", width=2)
            ban = 1 
        elif texto_actividad == "discurso":
            dibujo.rectangle([(388, 503), (405, 535)], fill="blue", width=2)
            ban = 0
        else:
            dibujo.rectangle([(388, 543), (406, 574)], fill="blue", width=2)
            ban = 1
        
        if ban == 0:
            dibujo.text((270, 203), nombre_mayuscula(texto_nombre), fill=(0, 0, 0), font=fuente)
        elif ban == 1:
            dibujo.text((270, 203), nombre_mayuscula(texto_nombre), fill=(0, 0, 0), font=fuente)
            dibujo.text((270, 264), nombre_mayuscula(texto_ayudante), fill=(0, 0, 0), font=fuente)

def asignacion_sala(a,b,dibujo):
    if a.get():
        dibujo.rectangle([(95, 712), (113, 734)], fill="blue", width=2)
    elif b.get():
        dibujo.rectangle([(95, 742),(113, 771)],fill="blue",width=2)