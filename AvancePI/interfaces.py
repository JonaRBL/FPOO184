from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image


ventana = Tk()
ventana.title("Date un roll UPQ")
ventana.geometry("600x510")

style = ttk.Style()


panel = ttk.Notebook(ventana)
panel.pack(fill= "both", expand = "yes")

pestana1 = tk.Frame(panel, background="red")
pestana2 = tk.Frame(panel, background="red")
pestana3 = tk.Frame(panel, background="red")
pestana4 = tk.Frame(panel, background="red")
pestana5 = tk.Frame(panel, background="red")
pestana6 = tk.Frame(panel, background="red")
pestana7 = tk.Frame(panel, background="red")
pestana8 = tk.Frame(panel, background="red")
pestana9 = tk.Frame(panel, background="red")
pestana10 = tk.Frame(panel, background="red")

#PESTAÑALT1
titulo = Label(pestana2, text = "LT1", bg = "red", fg = "blue", font = ("Times New Roman", 18)).place(x = 260,y = 0)

textLT1 = Label(pestana2, bg = "red", text = "Este edificio cuenta con lo siguiente:\nÁreas en planta baja:\nOficinas académicas de la dirección\nde programa educativo Ingeniería\nen Manufactura y cúbiculos para\ndocentes.\nÁreas en sotano:\nOficinas administrativas de recursos\nmateriales y servicios generales,\nalmacén general, taller de manufactura\ny área de enfermería.\nEspacios:\nTalleres de manufactura, materiales y\nelectrónica, sala 3D, cuarto de máquinas,\nsanitarios para hombres y mujeres\ny un sanitario mixto para personas\ncon discapacidad.", font=("Times New Roman", 16), justify ="left").place(x=0,y=28)
contacto = Label (pestana2, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 420)

canv = Canvas(pestana2, width=250, height=250, bg='white')
canv.place(x=330,y=28)
img = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\elet.jpg")
img = img.resize((250,250))
imag = ImageTk.PhotoImage(img)
canv.create_image(1,1,anchor=NW, image=imag)#20, 20, anchor=NW, image=img)

#PESTAÑATALLERES
titulo = Label(pestana3, text = "TALLERES", bg = "red", fg = "blue", font = ("Times New Roman", 18)).place(x = 260,y = 0)

textLT1 = Label(pestana3, bg = "red", text = "", font=("Times New Roman", 16), justify ="left").place(x=0,y=28)
contacto = Label (pestana3, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 420)

canv = Canvas(pestana3, width=250, height=250, bg='white')
canv.place(x=300,y=28)
img = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\elet.jpg")
img = img.resize((250,250))
imag = ImageTk.PhotoImage(img)
canv.create_image(1,1,anchor=NW, image=imag)#20, 20, anchor=NW, image=img)

#PESTAÑAEDIFICIOA
titulo = Label(pestana4, text = "LT1", bg = "red", fg = "blue", font = ("Times New Roman", 18)).place(x = 260,y = 0)

textLT1 = Label(pestana4, bg = "red", text = "Áreas en planta baja:\nRectoría, secretarías académica y\nadministrativa. Recursos humanos,\ncontabilida, abogado general\ny coordinación académica, cubículos\ndocentes de ingeniería\nmecatrónica.\nÁreas en planta alta:\nOficinas académicas de la dirección\nde programa educativo Ingeniería\nen mecatrónica, departamento\nde desarrollo humano.\nEspacios en planta baja:\nSala ", font=("Times New Roman", 16), justify ="left").place(x=0,y=28)
contacto = Label (pestana4, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 420)

canv = Canvas(pestana4, width=250, height=250, bg='white')
canv.place(x=300,y=28)
img = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\elet.jpg")
img = img.resize((250,250))
imag = ImageTk.PhotoImage(img)
canv.create_image(1,1,anchor=NW, image=imag)#20, 20, anchor=NW, image=img)

#PESTAÑAEDIFICIOB
titulo = Label(pestana5, text = "LT1", bg = "red", fg = "blue", font = ("Times New Roman", 18)).place(x = 260,y = 0)

textLT1 = Label(pestana5, bg = "red", text = "En este edificio se encuentran\nalgunos de los laboratorios de\nmanufactura, al igual que la\nsala 3D en donde se realizan\nconferencias, presentaciones de\nproyectos integradores entre\notras cosas, tambien en este\nedificio a finales del cuatrimestre\nse hacen las presentaciones de los\ntalleres cocurriculares de pintura,\nescultura y arte popular mexicano", font=("Times New Roman", 16), justify ="left").place(x=0,y=28)
contacto = Label (pestana5, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 310)

canv = Canvas(pestana5, width=250, height=250, bg='white')
canv.place(x=300,y=28)
img = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\elet.jpg")
img = img.resize((250,250))
imag = ImageTk.PhotoImage(img)
canv.create_image(1,1,anchor=NW, image=imag)#20, 20, anchor=NW, image=img)

#PESTAÑAEDIFICIOC
titulo = Label(pestana6, text = "LT1", bg = "red", fg = "blue", font = ("Times New Roman", 18)).place(x = 260,y = 0)

textLT1 = Label(pestana6, bg = "red", text = "En este edificio se encuentran\nalgunos de los laboratorios de\nmanufactura, al igual que la\nsala 3D en donde se realizan\nconferencias, presentaciones de\nproyectos integradores entre\notras cosas, tambien en este\nedificio a finales del cuatrimestre\nse hacen las presentaciones de los\ntalleres cocurriculares de pintura,\nescultura y arte popular mexicano", font=("Times New Roman", 16), justify ="left").place(x=0,y=28)
contacto = Label (pestana6, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 310)

canv = Canvas(pestana6, width=250, height=250, bg='white')
canv.place(x=300,y=28)
img = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\elet.jpg")
img = img.resize((250,250))
imag = ImageTk.PhotoImage(img)
canv.create_image(1,1,anchor=NW, image=imag)#20, 20, anchor=NW, image=img)

#PESTAÑACIDEA
titulo = Label(pestana7, text = "LT1", bg = "red", fg = "blue", font = ("Times New Roman", 18)).place(x = 260,y = 0)

textLT1 = Label(pestana7, bg = "red", text = "En este edificio se encuentran\nalgunos de los laboratorios de\nmanufactura, al igual que la\nsala 3D en donde se realizan\nconferencias, presentaciones de\nproyectos integradores entre\notras cosas, tambien en este\nedificio a finales del cuatrimestre\nse hacen las presentaciones de los\ntalleres cocurriculares de pintura,\nescultura y arte popular mexicano", font=("Times New Roman", 16), justify ="left").place(x=0,y=28)
contacto = Label (pestana7, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 310)

canv = Canvas(pestana7, width=250, height=250, bg='white')
canv.place(x=300,y=28)
img = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\elet.jpg")
img = img.resize((250,250))
imag = ImageTk.PhotoImage(img)
canv.create_image(1,1,anchor=NW, image=imag)#20, 20, anchor=NW, image=img)

#PESTAÑACAPTA
titulo = Label(pestana8, text = "LT1", bg = "red", fg = "blue", font = ("Times New Roman", 18)).place(x = 260,y = 0)

textLT1 = Label(pestana8, bg = "red", text = "En este edificio se encuentran\nalgunos de los laboratorios de\nmanufactura, al igual que la\nsala 3D en donde se realizan\nconferencias, presentaciones de\nproyectos integradores entre\notras cosas, tambien en este\nedificio a finales del cuatrimestre\nse hacen las presentaciones de los\ntalleres cocurriculares de pintura,\nescultura y arte popular mexicano", font=("Times New Roman", 16), justify ="left").place(x=0,y=28)
contacto = Label (pestana8, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 310)

canv = Canvas(pestana8, width=250, height=250, bg='white')
canv.place(x=300,y=28)
img = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\elet.jpg")
img = img.resize((250,250))
imag = ImageTk.PhotoImage(img)
canv.create_image(1,1,anchor=NW, image=imag)#20, 20, anchor=NW, image=img)

#PESTAÑACAFETERIA
titulo = Label(pestana9, text = "LT1", bg = "red", fg = "blue", font = ("Times New Roman", 18)).place(x = 260,y = 0)

textLT1 = Label(pestana9, bg = "red", text = "En este edificio se encuentran\nalgunos de los laboratorios de\nmanufactura, al igual que la\nsala 3D en donde se realizan\nconferencias, presentaciones de\nproyectos integradores entre\notras cosas, tambien en este\nedificio a finales del cuatrimestre\nse hacen las presentaciones de los\ntalleres cocurriculares de pintura,\nescultura y arte popular mexicano", font=("Times New Roman", 16), justify ="left").place(x=0,y=28)
contacto = Label (pestana9, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 310)

canv = Canvas(pestana9, width=250, height=250, bg='white')
canv.place(x=300,y=28)
img = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\elet.jpg")
img = img.resize((250,250))
imag = ImageTk.PhotoImage(img)
canv.create_image(1,1,anchor=NW, image=imag)#20, 20, anchor=NW, image=img)

#PESTAÑABIBLIOTECA
titulo = Label(pestana10, text = "LT1", bg = "red", fg = "blue", font = ("Times New Roman", 18)).place(x = 260,y = 0)

textLT1 = Label(pestana10, bg = "red", text = "En este edificio se encuentran\nalgunos de los laboratorios de\nmanufactura, al igual que la\nsala 3D en donde se realizan\nconferencias, presentaciones de\nproyectos integradores entre\notras cosas, tambien en este\nedificio a finales del cuatrimestre\nse hacen las presentaciones de los\ntalleres cocurriculares de pintura,\nescultura y arte popular mexicano", font=("Times New Roman", 16), justify ="left").place(x=0,y=28)
contacto = Label (pestana10, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 310)

canv = Canvas(pestana10, width=250, height=250, bg='white')
canv.place(x=300,y=28)
img = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\elet.jpg")
img = img.resize((250,250))
imag = ImageTk.PhotoImage(img)
canv.create_image(1,1,anchor=NW, image=imag)#20, 20, anchor=NW, image=img)

#PESTAÑAREGISTROUSUARIOS

panel.add(pestana1, text = "Registro de usuarios")
panel.add(pestana2, text = "LT1")
panel.add(pestana3, text = "Talleres")
panel.add(pestana4, text = "Edificio A")
panel.add(pestana5, text = "Edificio B")
panel.add(pestana6, text = "Edificio C")
panel.add(pestana7, text = "CIDEA")
panel.add(pestana8, text = "CAPTA")
panel.add(pestana9, text = "Cafeteria")
panel.add(pestana10, text = "Biblioteca")

ventana.mainloop()