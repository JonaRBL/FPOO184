from tkinter import Tk,Frame, PhotoImage, Menu
from tkinter import *
from ediA import *
from PIL import ImageTk, Image

edLt1 = Tk()
edLt1.title("LT1")
edLt1.geometry("600x400")

#2.Agregamos los Frames
seccion1 = Frame(edLt1, bg = "red")
seccion1.pack(expand = True, fill = 'both')

titulo = Label (seccion1, text = "LT1", bg = "White" ,width=50)
titulo.place(x = 0,y = 0)
titulo.configure(font=("Times New Roman", 16))

info = Label(seccion1,bg="red", text = "En este edificio se encuentran\nalgunos de los laboratorios de\nmanufactura, al igual que la\nsala 3D en donde se realizan\nconferencias, presentaciones de\nproyectos integradores entre\notras cosas, tambien en este\nedificio a finales del cuatrimestre\nse hacen las presentaciones de los\ntalleres cocurriculares de pintura,\nescultura y arte popular mexicano")
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

def Salir(edLt1):
    edLt1.destroy()
        
def CambiarVentanaLT1A():
    edLt1.destroy()
    ediA()

#img = PhotoImage(file="UPQ.png")
#imagi = Label(seccion1, image=img)
#imagi.place(x=300,y=50)

menubar = Menu(seccion1)
edLt1.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command( label="Edificio A", command=CambiarVentanaLT1A)
file_menu.add_command( label="Edificio B", )
file_menu.add_command( label="Edificio C")
file_menu.add_command( label="Biblioteca")
file_menu.add_command( label="CAPTA")
file_menu.add_command( label="CIDEA")
file_menu.add_command( label="Talleres")
file_menu.add_command( label="Cafeteria")
file_menu.add_separator()
file_menu.add_command(label="Regresar a la interfaz principal")
file_menu.add_command(label="Salir", command=Salir)
menubar.add_cascade(label='Edificios', menu=file_menu)



edLt1.mainloop()