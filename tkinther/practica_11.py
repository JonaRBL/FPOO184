from tkinter import Tk,Button,Frame, messagebox

def mostrarMensaje():
    messagebox.showinfo("¡¡AVISO!!", "Presionaste el boton azul")    

#1.Instanciamos el objeto ventana
ventana = Tk()
ventana.title("Ejemplo de 3 Frames")
ventana.geometry("600x400")

#2.Agregamos los Frames
seccion1 = Frame(ventana, bg = "red")
seccion1.pack(expand = True, fill = 'both')

seccion2 = Frame(ventana, bg = "purple")
seccion2.pack(expand = True, fill = 'both') 

seccion3 = Frame(ventana, bg = "blue")
seccion3.pack(expand = True, fill = 'both') 

#3.Agregamos botones
botonAzul = Button(seccion1, text = "Boton Azul", fg = "blue", command = mostrarMensaje)
botonAzul.place(x=60, y=60)

botonNegro = Button(seccion2, text = "Boton Negro", fg = "white", bg = "black")
botonNegro.grid(row = 0,column = 0)

botonAmarillo = Button(seccion2, text = "Boton Amarillo", bg = "#ffff4d")
botonAmarillo.grid(row = 1, column = 1)

botonVerde = Button(seccion3, text = "Boton Verde", bg ="green")
botonVerde.configure(height=2,width=10)
botonVerde.pack(side="left")

#llamamos al Main, siempre va al final del codigo
ventana.mainloop()
