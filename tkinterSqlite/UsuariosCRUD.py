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

#funcion para buscar un usuario
def ejecutaSelect():
    rsUsuario = controlador.consultaUsuario(varBus.get())
    
    for usu in rsUsuario:
        cadena = str(usu[0])+" "+ usu[1]+" "+ usu[2]+" "+ str(usu[3])
    
    if(rsUsuario):
        #print(cadena)
        textBus.insert("0.0", cadena)
    else:
        messagebox.showinfo("No encontrado", "Usuario no registardo en la BD")

def ejecutaConsulta():
    consult = controlador.consultasUsuarios()
    
    tabla.delete(*tabla.get_children())
    for user in consult:
        tabla.insert("", tk.END, text = "", values = user) 
    
        
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

#PESTAÑA2:Buscar usuario
titulo2 = Label(pestana2, text = "Buscar Usuario", fg = "red", font = ("Modern", 18)).pack()

varBus = tk.StringVar()
lblid = Label(pestana2, text = "Identificador de usuario: ").pack()
txtid = Entry(pestana2, textvariable = varBus).pack()

btnBusqueda = Button(pestana2, text = "Buscar", command = ejecutaSelect).pack()

subBus = Label(pestana2, text = "Registrado:", fg = "blue", font = ("Modern", 18)).pack()
textBus = tk.Text(pestana2, height = 5, width = 52)
textBus.pack()

#PESTAÑA3: Consultar usuarios
titulo3 = Label(pestana3, text = "Consultar Usuarios", fg = "red", font = ("Modern", 18)).pack()

btnConsulta = Button(pestana3, text = "Consulta", command = ejecutaConsulta).pack()

columns = ("id", "nombre", "correo", "contra")

tabla = ttk.Treeview(pestana3, columns = columns, show = "headings")

tabla.column("id", anchor=tk.W, width=50)
tabla.column("nombre", anchor=tk.W, width=150)
tabla.column("correo", anchor=tk.W, width=150)
tabla.column("contra", anchor=tk.W, width=200)

tabla.heading("id", text = "ID", )
tabla.heading("nombre", text = "NOMBRE")
tabla.heading("correo", text = "CORREO")
tabla.heading("contra", text = "CONTRASEÑA")

tabla.pack()

#accedemos al panel para agregar las pestañas
panel.add(pestana1, text = "Formulario de usuarios")
panel.add(pestana2, text = "Buscar Usuario")
panel.add(pestana3, text = "Consultar Usuarios")
panel.add(pestana4, text = "Actualizar Usuario")

ventana.mainloop()