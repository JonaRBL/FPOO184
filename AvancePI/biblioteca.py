from tkinter import Tk,Frame, PhotoImage,Menu
from tkinter import *
from funciones import cambiar_interfaz
from PIL import ImageTk, Image

BIBLIOTECA = Tk()
BIBLIOTECA.title("Biblioteca")
BIBLIOTECA.geometry("600x400")

#2.Agregamos los Frames
seccion1 = Frame(BIBLIOTECA, bg = "red")
seccion1.pack(expand = True, fill = 'both')

titulo = Label (seccion1, text = "Biblioteca", bg = "White" ,width=50)
titulo.place(x = 0,y = 0)
titulo.configure(font=("Times New Roman", 16))

info = Label(seccion1,bg="red", text = "El edificio cuenta con la tienda\nUPQ, donde se puede adquirir\nmercancía de la universidad tanto\ncomo materiales de papelería, así\nmismo se encuentran Servicios\nEscolares, mientras que en la\nparte superior el espacio esta\ndedicado    para aulas escolares.")
info.place(x = 10,y = 50)
info.configure(font=("Times New Roman", 16), justify ="left")

contacto = Label (seccion1, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150)
contacto.place(x = -250,y = 335)
contacto.configure(font=("Times New Roman", 10), justify = "left")

canv = Canvas(seccion1, width=250, height=250, bg='white')
canv.place(x=300,y=50)
img = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\bibliot.jpg")
img = img.resize((250,250))
imag = ImageTk.PhotoImage(img)

canv.create_image(1,1,anchor=NW, image=imag)#20, 20, anchor=NW, image=img)

menubar = Menu(seccion1)
BIBLIOTECA.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command( label="Edificio A")
file_menu.add_command( label="Edificio B")
file_menu.add_command( label="Edificio C")
file_menu.add_command( label="CAPTA")
file_menu.add_command( label="CIDEA")
file_menu.add_command( label="Talleres")
file_menu.add_command( label="Cafeteria")
file_menu.add_command( label="LT1")
file_menu.add_separator()
file_menu.add_command(label="Regresar a la interfaz principal")
menubar.add_cascade(label='Edificios', menu=file_menu)

BIBLIOTECA.mainloop()