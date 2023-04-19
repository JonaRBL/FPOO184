from tkinter import *
from tkinter import ttk
import tkinter as tk
from controlclases import *

controlador = controlaBD()

#proceder a guardar usuarios usando el metodo guardarUsuario() del objeto controlador
def ejecutaInsert():
    controlador.guardarCuenta(varCuen.get(), varSal.get())

def ejecutaConsulta():
    consult = controlador.consultasCuentas()
    
    tabla.delete(*tabla.get_children())
    for user in consult:
        tabla.insert("", tk.END, text = "", values = user)

def ejecutaActualizar():
    rsCuenta = controlador.consultaCuenta(varID.get())
    if(rsCuenta):
        controlador.actualizarCuenta(varID.get(), varaCue.get(), varaSal.get())
    else:
        messagebox.showinfo("No encontrado", "Cuenta no registrada en la BD")
        
ventana = Tk()
ventana.title("Cuentas del Banco")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill= "both", expand = "yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)

#PESTAÑA1:Formulario de cuentas
titulo = Label(pestana1, text = "Registro de Cuentas", fg = "blue", font = ("Modern", 18)).pack()

varCuen = tk.StringVar()
lblNom = Label(pestana1, text = "No. de Cuenta: ").pack()
txtNom = Entry(pestana1, textvariable = varCuen).pack()

varSal = tk.StringVar()
lblCor = Label(pestana1, text = "Saldo: ").pack()
txtCor = Entry(pestana1, textvariable = varSal).pack()

btnGuardar = Button(pestana1, text = "Guardar Cuenta", command = ejecutaInsert).pack()

#PESTAÑA2:Actualizar Cuenta
titulo2 = Label(pestana2, text = "Actualizar Cuenta", fg = "red", font = ("Modern", 18)).pack()

varID = tk.StringVar()
varaCue = tk.StringVar()
varaSal = tk.StringVar()
lblid = Label(pestana2, text = "Identificador de Cuenta: ").pack()
txtid = Entry(pestana2, textvariable = varID).pack()
lanNom = Label(pestana2, text = "Nuevo Numero de Cuenta: ").pack()
txNom = Entry(pestana2, textvariable = varaCue).pack()
lanCor = Label(pestana2, text = "Nuevo Saldo: ").pack()
txCor = Entry(pestana2, textvariable = varaSal).pack()

btnActuali = Button(pestana2, text = "Actualizar", command = ejecutaActualizar).pack()

#PESTAÑA3: Consultar usuarios
titulo3 = Label(pestana3, text = "Consultar Cuentas", fg = "red", font = ("Modern", 18)).pack()

btnConsulta = Button(pestana3, text = "Consulta", command = ejecutaConsulta).pack()

columns = ("id", "cuenta", "saldo")

tabla = ttk.Treeview(pestana3, columns = columns, show = "headings")

tabla.column("id", anchor=tk.W, width=50)
tabla.column("cuenta", anchor=tk.W, width=150)
tabla.column("saldo", anchor=tk.W, width=150)

tabla.heading("id", text = "IDCuenta", )
tabla.heading("cuenta", text = "NoCuenta")
tabla.heading("saldo", text = "Saldo")

tabla.pack()

panel.add(pestana1, text = "Formulario de Cuenta")
panel.add(pestana2, text = "Actualizar Cuenta")
panel.add(pestana3, text = "Consultar Cuentas")

ventana.mainloop()