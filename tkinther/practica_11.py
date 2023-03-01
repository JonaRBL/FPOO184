from tkinter import Tk,Button,Frame, messagebox


#5.Declaramos funcion para los mensajes
def mostrarMensaje():
    messagebox.showinfo("¡¡AVISO!!", "Presionaste el boton azul")
    messagebox.showerror("ERROR", "Todo fallo con exito :|")
    messagebox.askokcancel("Pregunta", "¿El jugó con tu corazon?")
    messagebox.askquestion(":0", "¿soportas panzona?")
    messagebox.askretrycancel("veremos", "o no puedes?")
    messagebox.askyesno("cariñosos", "¿vamos a los cariños?")
    messagebox.askyesnocancel("viaje", "pueblito magico o que?")
    #investigar hacer input a traves del mensaje con caja de texto para colocar respuesta
    
#6.Funcion para agregar botones
def agregarBoton():
    botonVerde.config(text = "+", bg = "green", fg = "white", )
    botonNuevo = Button(seccion3, text = "Nuevo")
    botonNuevo.pack()

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
#4.Posicionamiento de elementos(place,grid,pack)
botonAzul = Button(seccion1, text = "Boton Azul", fg = "blue", command = mostrarMensaje)
botonAzul.place(x=60, y=60)

botonNegro = Button(seccion2, text = "Boton Negro", fg = "white", bg = "black")
botonNegro.grid(row = 0,column = 0)

botonAmarillo = Button(seccion2, text = "Boton Amarillo", bg = "#ffff4d")
botonAmarillo.grid(row = 1, column = 1)

botonVerde = Button(seccion3, text = "Boton Verde", fg ="black", command = agregarBoton)
botonVerde.configure(height=2,width=10)
botonVerde.pack(side="left")

#llamamos al Main, siempre va al final del codigo
ventana.mainloop()
