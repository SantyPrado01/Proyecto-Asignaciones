from tkinter import *
from funciones import *

ventana = Tk()

ventana.title('Jw Planillas')

boton_asignaciones = Button(text='Asignaciones Estudiantiles', command=ejecutar_menu_asignaciones)
boton_asignaciones.grid(row=0, column=0)

boton_predicaciones = Button(text='Asignaciones Predicacion')
boton_predicaciones.grid(row=0, column=1)

boton_acomodadores = Button(text='Asingaciones Acomodadores')
boton_acomodadores.grid(row=1, column=0)

boton_microfonistas = Button(text='Asignaciones Microfonistas')
boton_microfonistas.grid(row=1, column=1)

ventana.mainloop()