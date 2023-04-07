from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControlBD import *


controlador = controladorBD()

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varAP.get(),varAM.get(),varED.get(),varCor.get())

Ventana=Tk()
Ventana.title("UNIVERSIDAD POLITECNICA DE QUERÉTARO")
Ventana.geometry("500x300")


panel=ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1=ttk.Frame(panel)
titulo= Label(pestana1,text="Registra tu acceso UPQ", fg="red", font=("Arial",18)).pack()

varNom= tk.StringVar()
iblNom= Label(pestana1, text="Nombre(s): ").pack()
txtNom= Entry(pestana1, textvariable=varNom).pack()

varAP= tk.StringVar()
iblAP= Label(pestana1, text="Apellido Paterno: ").pack()
txtAP= Entry(pestana1, textvariable=varAP).pack()

varAM= tk.StringVar()
iblAM= Label(pestana1, text="Apellido Materno: ").pack()
txtAM= Entry(pestana1, textvariable=varAM).pack()

varED= tk.StringVar()
iblED= Label(pestana1, text="Edad: ").pack()
txtED= Entry(pestana1, textvariable=varED).pack()

varCor= tk.StringVar()
iblCor= Label(pestana1, text="Correo electronico: ").pack()
txtCor= Entry(pestana1, textvariable=varCor).pack()


btnGuardar= Button(pestana1, text="Acceder",command=ejecutaInsert).pack()


panel.add(pestana1,text="Acceso Usuarios")

Ventana.mainloop()