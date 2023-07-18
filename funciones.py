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
            dibujo.rectangle([(53, 298), (65, 309)], fill="blue", width=2)
            ban = 0
        elif texto_actividad == "primera conversacion":
            dibujo.rectangle([(53, 320), (65, 331)], fill="blue", width=2)
            ban = 1
        elif texto_actividad == "revisita":
            dibujo.rectangle([(53, 365), (65, 376)], fill="blue", width=2)
            ban = 1
        elif texto_actividad == "curso biblico":
            dibujo.rectangle([(305, 298), (317, 309)], fill="blue", width=2)
            ban = 1 
        elif texto_actividad == "discurso":
            dibujo.rectangle([(305, 320), (317, 331)], fill="blue", width=2)
            ban = 0
        else:
            dibujo.text([(305, 343),(317, 354)], fill='blue', width=2)
            ban = 1
        if ban == 0:
            dibujo.text((136, 93), nombre_mayuscula(texto_nombre), fill=(0, 0, 0), font=fuente)
        elif ban == 1:
            dibujo.text((136, 93), nombre_mayuscula(texto_nombre), fill=(0, 0, 0), font=fuente)
            dibujo.text((155, 142), nombre_mayuscula(texto_ayudante), fill=(0, 0, 0), font=fuente)

def asignacion_sala(a,b,dibujo):
    if a.get():
        dibujo.rectangle([(53, 450), (65, 461)], fill="blue", width=2)
    elif b.get():
        dibujo.rectangle([(53, 473),(65, 484)],fill="blue",width=2)