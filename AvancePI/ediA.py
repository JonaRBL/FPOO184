from tkinter import Tk,Frame, PhotoImage,Menu
from tkinter import *
from PIL import ImageTk, Image
from ediB import *

class ediA():
    
    def __init__(self):    
        self.edifA = Tk()
        self.edifA.title("Edificio A")
        self.edifA.geometry("600x400")
        
    #2.Agregamos los Frames
        self.seccion1 = Frame(self.edifA, bg = "red")
        self.seccion1.pack(expand = True, fill = 'both')

        self.titulo = Label (self.seccion1, text = "Edificio A", bg = "White" ,width=50)
        self.titulo.place(x = 0,y = 0)
        self.titulo.configure(font=("Times New Roman", 16))

        self.info = Label(self.seccion1,bg="red", text = "En este edificio se encuentran\nalgunos de los laboratorios de\nmanufactura, al igual que la\nsala 3D en donde se realizan\nconferencias, presentaciones de\nproyectos integradores entre\notras cosas, tambien en este\nedificio a finales del cuatrimestre\nse hacen las presentaciones de los\ntalleres cocurriculares de pintura,\nescultura y arte popular mexicano")
        self.info.place(x = 10,y = 50)
        self.info.configure(font=("Times New Roman", 16), justify ="left")

        self.contacto = Label (self.seccion1, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150)
        self.contacto.place(x = -250,y = 335)
        self.contacto.configure(font=("Times New Roman", 10), justify = "left")

        canv = Canvas(self.seccion1, width=250, height=250, bg='white')
        canv.place(x=300,y=50)
        img = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\edificioA.jpg")
        img = img.resize((250,250))
        imag = ImageTk.PhotoImage(img)

        canv.create_image(1,1,anchor=NW, image=imag)#20, 20, anchor=NW, image=img)
        
        def CambiarVentana2():
            self.edifA.destroy()
            ediB()
        def Salir():
            self.edifA.destroy()
        def CambiarVentana1():
            self.edLt1.destroy()
            ediA()

        self.menubar = Menu(self.seccion1)
        self.edifA.config(menu=self.menubar)
        self.file_menu = Menu(self.menubar, tearoff=False)
        self.file_menu.add_command( label="Edificio B", command=CambiarVentana2)
        self.file_menu.add_command( label="Edificio C")
        self.file_menu.add_command( label="Biblioteca")
        self.file_menu.add_command( label="CIDEA")
        self.file_menu.add_command( label="Talleres")
        self.file_menu.add_command( label="Cafeteria")
        self.file_menu.add_command( label="LT1", command=CambiarVentana1)
        self.file_menu.add_command( label="CAPTA")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Regresar a la interfaz principal")
        self.file_menu.add_command(label="Salir", command=Salir)
        self.menubar.add_cascade(label='Edificios', menu=self.file_menu)
    
        self.edifA.mainloop()