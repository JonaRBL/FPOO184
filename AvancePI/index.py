from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
from ControlBD import *

ventana = Tk()
ventana.title("Date un roll UPQ")
ventana.geometry("600x530")

style = ttk.Style()


panel = ttk.Notebook(ventana)
panel.pack(fill= "both", expand = "yes")

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
titulo = Label(pestana2, text = "LT1", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textLT1 = Label(pestana2, bg = "red", text = "Este edificio cuenta con lo siguiente:\nÁreas en planta baja:\nOficinas académicas de la dirección de\nprograma educativo Ingeniería en\nManufactura y cúbiculos para docentes.\nÁreas en sotano:\nOficinas administrativas de recursos\nmateriales y servicios generales, almacén\ngeneral, taller de manufactura y área de\nenfermería.\nEspacios:\nTalleres de manufactura, materiales y\nelectrónica, sala 3D, cuarto de máquinas, sanitarios para hombres y mujeres y\nun sanitario mixto para personas con discapacidad.", font=("Times New Roman", 14), justify ="left").place(x=0,y=28)
contacto = Label (pestana2, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvL1 = Canvas(pestana2, width=250, height=250, bg='white')
canvL1.place(x=330,y=28)
imgL = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\elet.jpg")
imgL = imgL.resize((250,250))
imagL = ImageTk.PhotoImage(imgL)
canvL1.create_image(1,1,anchor=NW, image=imagL)#20, 20, anchor=NW, image=img)

#PESTAÑATALLERES
titulo = Label(pestana3, text = "TALLERES", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textTA = Label(pestana3, bg = "red", text = "En este edificio se llevan a cabo los\ntalleres culturales de danza\ncontemporánea, baile jazz, hip hop,\nbaile de salón, danza folclórica, al\nigual aquí se llevan acabo los\nentrenamientos del representativo de\ntaekwondo, hip hop, y también aquí se\nencuentran las duchas para hombres y\npara mujeres, y también cuenta con un\ngimnasio en donde asisten\nprincipalmente representativos\ndeportivos y alumnado de la\nuniversidad.", font=("Times New Roman", 14), justify ="left").place(x=0,y=28)
contacto = Label (pestana3, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvTA = Canvas(pestana3, width=250, height=250, bg='white')
canvTA.place(x=300,y=28)
imgTA = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\talleres.jpg")
imgTA = imgTA.resize((250,250))
imagTA = ImageTk.PhotoImage(imgTA)
canvTA.create_image(1,1,anchor=NW, image=imagTA)#20, 20, anchor=NW, image=img)

#PESTAÑAEDIFICIOA
titulo = Label(pestana4, text = "EDIFICIO A", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textEA = Label(pestana4, bg = "red", text = "Áreas en planta baja:\nRectoría, secretarías académica y\nadministrativa. Recursos humanos,\ncontabilida, abogado general y\ncoordinación académica, cubículos\ndocentes de ingeniería mecatrónica.\nÁreas en planta alta:\nOficinas académicas de la dirección de\nprograma educativo Ingeniería en\nmecatrónica, departamento de desarrollo\nhumano.\nEspacios en planta baja:\nSala de videoconferencia, laboratorio multidisciplinario, laboratorio de química,\n5 aulas para impartición de clase, sanitarios para hombres y mujeres.\nEspacios en planta alta:\n9 aulas para imparticion de clases, laboratorios de computo 1, 2 y 3, site de la\ndirección de tecnologías de información y telecomunicaciones, site de cámaras\nde vigilancia, sanitarios y sala de ciencias básicas. ", font=("Times New Roman", 14), justify ="left").place(x=0,y=28)
contacto = Label (pestana4, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvEA = Canvas(pestana4, width=250, height=250, bg='white')
canvEA.place(x=330,y=28)
imgEA = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\edificioA.jpg")
imgEA = imgEA.resize((250,250))
imagEA = ImageTk.PhotoImage(imgEA)
canvEA.create_image(1,1,anchor=NW, image=imagEA)#20, 20, anchor=NW, image=img)

#PESTAÑAEDIFICIOB
titulo = Label(pestana5, text = "EDIFICIO B", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textEB = Label(pestana5, bg = "red", text = "Áreas en planta alta:\nOficinas académicas de la dirección de\nprograma educativo de negocios\ninternacinales, dirección de programa\neducativo de administración y gestión de\npequeñas y medianas empresas, cubículos\nde docentes.\nEspacios en planta baja:\nSala isóptica, aula-auditorio, laboratorios\nde cómputo 1 y 2, 8 aulas para impartición\nde clase, papelería, sanitarios para hombres\ny mujeres, y un sanitario para hombres y\nuno para mujeres adecuado para personas con discapacidad.\nEspacios en planta alta:\nSalón de usos múltiples, sala de juntas, 8 aulas para impartición de clases,\nsanitarios para hombres y mujeres y un sanitario para hombres y uno para\nmujeres adecuado para personas con discapacidad.", font=("Times New Roman", 14), justify ="left").place(x=0,y=28)
contacto = Label (pestana5, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvEB = Canvas(pestana5, width=250, height=250, bg='white')
canvEB.place(x=330,y=28)
imgEB = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\edificioB.jpg")
imgEB = imgEB.resize((250,250))
imagEB = ImageTk.PhotoImage(imgEB)
canvEB.create_image(1,1,anchor=NW, image=imagEB)#20, 20, anchor=NW, image=img)

#PESTAÑAEDIFICIOC
titulo = Label(pestana6, text = "EDIFICIO C", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textEC = Label(pestana6, bg = "red", text = "Áreas en planta baja:\nOficina administrativa de control de\nlaboratorios de redes.\nÁreas en planta alta:\nOficinas académicas de dirección de\nprograma educativo ingeniería en sistemas\ncomputacionales, dirección de programa\neducativo redes y telecomunicaciones y\ncubículos de docentes.\nEspacios en planta baja:\nSala isóptica, aula-auditorio, Laboratorios\nde telemática, de redes, CONACyT y de\ncómputo, 8 aulas para impartición de clase sanitarios para hombres y mujeres,\ny un sanitario para hombres y uno para mujeres adecuado para personas con\ndiscapacidad.\nEspacios en planta alta:\nLaboratorio de cómputo, 8 aulas para impartición de clase, sanitarios para\nhombres y mujeres, y un sanitario para hombres y uno para mujeres adecuado\npara personas con discapacidad, elevador.", font=("Times New Roman", 14), justify ="left").place(x=0,y=28)
contacto = Label (pestana6, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvEC = Canvas(pestana6, width=250, height=250, bg='white')
canvEC.place(x=330,y=28)
imgEC = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\edificioC.jpg")
imgEC = imgEC.resize((250,250))
imagEC = ImageTk.PhotoImage(imgEC)
canvEC.create_image(1,1,anchor=NW, image=imagEC)#20, 20, anchor=NW, image=img)

#PESTAÑACIDEA
titulo = Label(pestana7, text = "CIDEA", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textCI = Label(pestana7, bg = "red", text = "Áreas en planta baja:\nOficinas administrativas del programa\neducativo de ingeniería en tecnología\nautomotriz, oficinas administrativas de\ntalleres y laboratorios pesados, oficina\nBrose.\nÁreas en planta alta:\nOficinas administrativas de la dirección de\ninvestigación y posgrado, dirección de\nplaneación, órgano interno de control.\nEspacios en planta baja:\nLaboratorio de manufactura aditiva e\ningeniería inversa, 4 aulas para la impartición de clases, sanitarios para hombres\ny mujeres, y un sanitario para hombres y uno para mujeres adecuado para\npersonas con discapacidad.\nEspacios en planta alta:\nSala de juntas de CIDEA, sala de acuerdos CIDEA.", font=("Times New Roman", 14), justify ="left").place(x=0,y=28)
contacto = Label (pestana7, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvCI = Canvas(pestana7, width=250, height=250, bg='white')
canvCI.place(x=330,y=28)
imgCI = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\fcidea.jpg")
imgCI = imgCI.resize((250,250))
imagCI = ImageTk.PhotoImage(imgCI)
canvCI.create_image(1,1,anchor=NW, image=imagCI)#20, 20, anchor=NW, image=img)

#PESTAÑACAPTA
titulo = Label(pestana8, text = "CAPTA", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textCA = Label(pestana8, bg = "red", text = "Áreas en planta baja:\nAulas académicas\nÁreas de planta alta:\nAulas académicas.\nEspacios en planta baja:\n7 aulas para impartir clases, sanitarios para\nhombres y mujeres, y un sanitario para\nhombres y uno para mujeres adecuado para\npersonas con discapacidad.\nEspacios en planta alta:\n7 aulas para impartir clases, oficina-almacén\nde talleres pesados, sanitarios para\nhombres y mujeres, y un sanitario para hombres y uno para mujeres adecuado\npara personas con discapacidad.", font=("Times New Roman", 14), justify ="left").place(x=0,y=28)
contacto = Label (pestana8, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvCA = Canvas(pestana8, width=250, height=250, bg='white')
canvCA.place(x=330,y=28)
imgCA = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\fcapta.jpg")
imgCA = imgCA.resize((250,250))
imagCA = ImageTk.PhotoImage(imgCA)
canvCA.create_image(1,1,anchor=NW, image=imagCA)#20, 20, anchor=NW, image=img)

#PESTAÑACAFETERIA
titulo = Label(pestana9, text = "LA KAFE", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textKF = Label(pestana9, bg = "red", text = "Áreas:\nOficinas administrativas del servicio de\ncomedor.\nEspacios en planta baja:\nCocina, cafetería, anexos de cafetería,\nOXXO, sanitarios para hombres y mujeres,\ny un sanitario para hombres y uno para\nmujeres adecuado para personas con\ndiscapacidad.\nEspacios en sótano:\nAlmacén general.", font=("Times New Roman", 14), justify ="left").place(x=0,y=28)
contacto = Label (pestana9, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvKF = Canvas(pestana9, width=250, height=250, bg='white')
canvKF.place(x=330,y=28)
imgKF = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\lakafe.jpg")
imgKF = imgKF.resize((250,250))
imagKF = ImageTk.PhotoImage(imgKF)
canvKF.create_image(1,1,anchor=NW, image=imagKF)#20, 20, anchor=NW, image=img)

#PESTAÑABIBLIOTECA
titulo = Label(pestana10, text = "BIBLIOTECA", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textBI = Label(pestana10, bg = "red", text = "El edificio cuenta con la tienda UPQ, donde\nse puede adquirir mercancía de la\nuniversidad tanto como materiales de\npapelería, así mismo se encuentran\nServicios Escolares, mientras que en la\nparte superior el espacio esta dedicado\npara aulas escolares.", font=("Times New Roman", 14), justify ="left").place(x=0,y=28)
contacto = Label (pestana10, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=150, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvBI = Canvas(pestana10, width=250, height=250, bg='white')
canvBI.place(x=330,y=28)
imgBI = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\bibliot.jpg")
imgBI = imgBI.resize((250,250))
imagBI = ImageTk.PhotoImage(imgBI)
canvBI.create_image(1,1,anchor=NW, image=imagBI)#20, 20, anchor=NW, image=img)

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