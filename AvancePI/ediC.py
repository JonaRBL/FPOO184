from tkinter import Tk,Frame, PhotoImage,Menu
from tkinter import *
from funciones import cambiar_interfaz

edifC = Tk()
edifC.title("edificio A")
edifC.geometry("600x400")

#2.Agregamos los Frames
seccion1 = Frame(edifC, bg = "red")
seccion1.pack(expand = True, fill = 'both')

titulo = Label (seccion1, text = "Edificio a", bg = "White" ,width=50)
titulo.place(x = 0,y = 0)
titulo.configure(font=("Times New Roman", 16))

info = Label(seccion1,bg="red", text = "En este edificio se encuentran\nalgunos de los laboratorios de\nmanufactura, al igual que la\nsala 3D en donde se realizan\nconferencias, presentaciones de\nproyectos integradores entre\notras cosas, tambien en este\nedificio a finales del cuatrimestre\nse hacen las presentaciones de los\ntalleres cocurriculares de pintura,\nescultura y arte popular mexicano")
info.place(x = 10,y = 50)
info.configure(font=("Times New Roman", 16), justify ="left")

contacto = Label (seccion1, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150)
contacto.place(x = -250,y = 335)
contacto.configure(font=("Times New Roman", 10), justify = "left")

img = PhotoImage(file="UPQ.png")
imagi = Label(seccion1, image=img)
imagi.place(x=300,y=50)

menubar = Menu(seccion1)
edifC.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command( label="Edificio A")
file_menu.add_command( label="Edificio B")
file_menu.add_command( label="Biblioteca")
file_menu.add_command( label="CAPTA")
file_menu.add_command( label="CIDEA")
file_menu.add_command( label="Talleres")
file_menu.add_command( label="Cafeteria")
file_menu.add_command( label="LT1")
file_menu.add_separator()
file_menu.add_command(label="Regresar a la interfaz principal")
menubar.add_cascade(label='Edificios', menu=file_menu)

edifC.mainloop()