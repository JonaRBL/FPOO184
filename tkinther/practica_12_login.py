from tkinter import *
from tkinter import messagebox
from funci import acceso

ventana = Tk()
User = StringVar()
Password = StringVar()

def crearVentana():
    
    ventana.title("Login(Practica 12)")
    ventana.geometry("600x400")
    
    seccion1 = Frame(ventana, bg = "blue")
    seccion1.pack(expand = True, fill = 'both')
    
    pedUsu = Label(seccion1, text = "Acceder a la cuenta", bg = "blue", fg = "white").pack(side = "top")
    
    vacio= Label(seccion1, text = " ", bg = "blue").pack(side = "top")
    
    Corr = Label(seccion1, text = "Correo o usuario:",bg = "blue", fg = "white").pack(side = "top")
    
    User.set("")
    InUsu = Entry(seccion1, textvariable = User).pack(side = "top")
    
    Cont = Label(seccion1, text = "Contraseña:", bg = "blue", fg = "white").pack(side = "top")
    
    Password.set("")
    InPass = Entry(seccion1, textvariable = Password, show = "*").pack(side = "top")
    
    Ingresar = Button(seccion1, text = "Ingresar", bg = "yellow", fg = "black", command = ingreso).pack(side = "top")
    
    ventana.mainloop()
    
def ingreso():
    prueba = usu1.conect(Password.get())
    if prueba:
        messagebox.showinfo("Ingreso", "Se ingresa con exito")
    else:
        messagebox.showerror("ERROR", "Ingreso denegado, revise sus credenciales")

if __name__ == "__main__":
    usu1 = acceso("Soportapanzona", "Jonathan2701")
    crearVentana()
    
    