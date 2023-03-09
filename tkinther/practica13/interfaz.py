from tkinter import Tk,Button, messagebox
from tkinter import *
import random
import string

ventana = Tk()
ventana.title("Generador de contraseña")
ventana.geometry("600x400")
ventana.config(bg  ="blue")

titLongi = Label(ventana, text = "Longitud de la contraseña",bg = "black", fg = "white")
titLongi.grid(row = 0, column = 0)

pedirLongi = Entry(ventana, width = 10)
pedirLongi.insert(0,"8")
pedirLongi.grid(row = 0,column = 1)

mayus = IntVar()
botonNegro = Checkbutton(ventana, text = "Mayusculas", fg = "white", bg = "black", variable=mayus)
botonNegro.grid(row = 1, column = 0)

Espcara = IntVar()
boton2 = Checkbutton(ventana, text = "Caracteres especiales", fg = "white", bg = "black", variable=Espcara)
boton2.grid(row = 2, column = 0)


botonBlanco = Button(ventana, text = "Generar contraseña", fg = "white", bg = "black")
botonBlanco.grid(row = 3, column = 1)

botonAmarillo = Button(ventana, text = "Comprobar fortaleza", fg = "black", bg = "yellow")
botonAmarillo.grid(row = 3, column = 0)

contrasenaGenerada = Label(ventana, text="")
contrasenaGenerada.grid(row = 4,column = 0)

ventana.mainloop()