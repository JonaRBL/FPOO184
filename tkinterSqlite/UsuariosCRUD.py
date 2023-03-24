from tkinter import *
from tkinter import ttk
import tkinter as tk

#importamos las clases creadas a la ventana
from controladorBD import *

#Creamos un objeto de tipo controlador
controlador = controladorBD()

#proceder a guardar usuarios usando el metodo guardarUsuario() del objeto controlador

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())

ventana = Tk()
ventana.title("CRUD usuarios")
ventana.geometry("500x300")

#creamos el notebook
panel = ttk.Notebook(ventana)
panel.pack(fill= "both", expand = "yes")

#pestañas que tendra el notebook
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

#PESTAÑA1:Formulario de usuarios
titulo = Label(pestana1, text = "Registro de Usuarios", fg = "blue", font = ("Modern", 18)).pack()

varNom = tk.StringVar()
lblNom = Label(pestana1, text = "Nombre: ").pack()
txtNom = Entry(pestana1, textvariable = varNom).pack()

varCor = tk.StringVar()
lblCor = Label(pestana1, text = "Correo: ").pack()
txtCor = Entry(pestana1, textvariable = varCor).pack()

varCon = tk.StringVar()
lblCon = Label(pestana1, text = "Contraseña: ").pack()
txtCon = Entry(pestana1, textvariable = varCon, show = "*").pack()

btnGuardar = Button(pestana1, text = "Guardar Usuario", command = ejecutaInsert).pack()

#accedemos al panel para agregar las pestañas
panel.add(pestana1, text = "Formulario de usuarios")
panel.add(pestana2, text = "Buscar Usuario")
panel.add(pestana3, text = "Consultar Usuarios")
panel.add(pestana4, text = "Actualizar Usuario")

ventana.mainloop()