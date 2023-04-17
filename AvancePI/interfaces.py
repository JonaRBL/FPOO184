from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
from ControlBD import *


controlador = controladorBD()

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varAP.get(),varAM.get(),varED.get(),varCor.get())

def ejecutaInsert2():
    controlador.guardarMaterial(varMat.get(), varCan.get())

#funcion para buscar un usuario
def ejecutaSelect():
    rsMaterial = controlador.consultaMaterial(varBusmat.get())
    
    for mater in rsMaterial:
        cadena = str(mater[0])+" "+ mater[1]+" "+ str(mater[2])
    
    if(rsMaterial):
        #print(cadena)
        textBus.insert("0.0", cadena)
    else:
        messagebox.showinfo("No encontrado", "Material no registardo en la BD")

def ejecutaConsulta():
    consult = controlador.consultasMateriales()
    
    tabla.delete(*tabla.get_children())
    for user in consult:
        tabla.insert("", tk.END, text = "", values = user)

def ejecutaActualizar():
    rsMaterial = controlador.consultaMaterial(varIDmat.get())
    if(rsMaterial):
        controlador.actualizarMaterial(varIDmat.get(), varaMat.get(), varaCan.get())
    else:
        messagebox.showinfo("No encontrado", "Material no registardo en la BD")
def ejecutaBusqueda():
    rsMaterial = controlador.consultaMaterial(varID2.get())
    
    textBus2.delete("1.0", "end")
    for usu in rsMaterial:
        cadena = str(usu[0])+" "+ usu[1]+" "+ str(usu[2])
    
    if(rsMaterial):
        #print(cadena)
        textBus2.insert("0.0", cadena)
    else:
        messagebox.showinfo("No encontrado", "Material no registardo en la BD")

def ejecutaEliminar():
    sel = messagebox.askyesno("Elimiar registro", "Seguro que desea eliminar el registro?")
    if (sel == True):
        
        try:
            controlador.eliminarMaterial(varID2.get())
        except sqlite3.OperationalError:
            print("Error de Consulta")

ventana = Tk()
ventana.title("Date un roll UPQ")
ventana.geometry("900x530")

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
pestana11 = ttk.Frame(panel)
pestana12 = ttk.Frame(panel)
pestana13 = ttk.Frame(panel)
pestana14 = ttk.Frame(panel)
pestana15 = ttk.Frame(panel)

#PESTAÑALT1
titulo = Label(pestana2, text = "LT1", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textLT1 = tk.Text(pestana2, font=("Times New Roman", 14), bg="red",height = 11, width = 55)
texto1= """Este edificio cuenta con lo siguiente:
Áreas en planta baja:
Oficinas académicas de la dirección de programa educativo 
Ingeniería en Manufactura y cúbiculos para docentes.
Áreas en sotano:
Oficinas administrativas de recursos materiales y servicios generales, almacén general, taller de manufactura y área de enfermería.
Espacios:
Talleres de manufactura, materiales y electrónica, sala 3D, cuarto de máquinas, sanitarios para hombres y mujeres y un sanitario 
mixto para personas con discapacidad."""
textLT1.insert(tk.END, texto1)
textLT1.configure(state = tk.DISABLED)
textLT1.place(x=0,y=28)
contacto = Label (pestana2, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=200, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvL1 = Canvas(pestana2, width=350, height=350, bg='white')
canvL1.place(x=520,y=28)
imgL = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\elet.jpg")
imgL = imgL.resize((350,350))
imagL = ImageTk.PhotoImage(imgL)
canvL1.create_image(1,1,anchor=NW, image=imagL)#20, 20, anchor=NW, image=img)

#PESTAÑATALLERES
titulo = Label(pestana3, text = "TALLERES", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textTA = tk.Text(pestana3, font=("Times New Roman", 14), bg="red",height = 7, width = 55)
texto2 = """En este edificio se llevan a cabo los talleres culturales de danza 
contemporánea, baile jazz, hip hop, baile de salón y danza 
folclórica, al igual aquí se llevan acabo los entrenamientos de los 
representativos de taekwondo, hip hop, en donde tambien se 
encuentran las duchas para hombres y para mujeres, también 
cuenta con un gimnasio en donde asisten principalmente 
representativos deportivos y alumnado de la universidad."""
textTA.insert(tk.END, texto2)
textTA.configure(state = tk.DISABLED)
textTA.place(x=0,y=28)
contacto = Label (pestana3, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=200, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvTA = Canvas(pestana3, width=350, height=350, bg='white')
canvTA.place(x=520,y=28)
imgTA = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\talleres.jpg")
imgTA = imgTA.resize((350,350))
imagTA = ImageTk.PhotoImage(imgTA)
canvTA.create_image(1,1,anchor=NW, image=imagTA)#20, 20, anchor=NW, image=img)

#PESTAÑAEDIFICIOA
titulo = Label(pestana4, text = "EDIFICIO A", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textEA = tk.Text(pestana4, font=("Times New Roman", 14), bg="red",height = 16, width = 55)
texto3 ="""Áreas en planta baja:
Rectoría, Secretarías Académica y Administrativa, Recursos
Humanos, Contabilidad, Abogado General y Coordinación
Académica, Cubículos docentes de Ingeniería Mecatrónica.
Áreas en planta alta:
Oficinas académicas de la Dirección de Programa Educativo
Ingeniería en Mecatrónica, Departamento de Desarrollo Humano.
Espacios en planta baja:
Sala de videoconferencia, laboratorio multidisciplinario, 
laboratorio de Química, 5 aulas para impartición de clase, 
sanitarios para hombres y mujeres.
Espacios en planta alta:
9 Aulas para impartición de clases, laboratorios de cómputo 1, 2 y
3, site de la Dirección de Tecnologías de Información y
Telecomunicaciones, site de cámaras de vigilancia, sanitarios y
sala de Ciencias Básicas."""
textEA.insert(tk.END, texto3)
textEA.configure(state = tk.DISABLED)
textEA.place(x=0,y=28)
contacto = Label (pestana4, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=200, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvEA = Canvas(pestana4, width=350, height=350, bg='white')
canvEA.place(x=520,y=28)
imgEA = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\edificioA.jpg")
imgEA = imgEA.resize((350,350))
imagEA = ImageTk.PhotoImage(imgEA)
canvEA.create_image(1,1,anchor=NW, image=imagEA)#20, 20, anchor=NW, image=img)

#PESTAÑAEDIFICIOB
titulo = Label(pestana5, text = "EDIFICIO B", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textEB = tk.Text(pestana5, font=("Times New Roman", 14), bg="red",height = 15, width = 55)
texto4 ="""Áreas en planta alta:
Oficinas académicas de la Dirección de Programa Educativo de
Negocios Internacionales, Dirección de Programa Educativo de
Administración y Gestión de Pequeñas y Medianas Empresas,
Cubículos de docentes.
Espacios en planta baja:
Sala isóptica, aula-auditorio, laboratorios de cómputo 1 y 2, 8 
aulas para impartición de clase, papelería, sanitarios para hombres 
y mujeres, y un sanitario para hombres y uno para mujeres
adecuado para personas con discapacidad.
Espacios en planta alta:
Salón de usos múltiples, sala de juntas, 8 aulas para impartición de
clases, sanitarios para hombres y mujeres y un sanitario para
hombres y uno para mujeres adecuado para personas con
discapacidad."""
textEB.insert(tk.END, texto4)
textEB.configure(state = tk.DISABLED)
textEB.place(x=0,y=28)
contacto = Label (pestana5, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=200, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvEB = Canvas(pestana5, width=350, height=350, bg='white')
canvEB.place(x=520,y=28)
imgEB = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\edificioB.jpg")
imgEB = imgEB.resize((350,350))
imagEB = ImageTk.PhotoImage(imgEB)
canvEB.create_image(1,1,anchor=NW, image=imagEB)#20, 20, anchor=NW, image=img)

#PESTAÑAEDIFICIOC
titulo = Label(pestana6, text = "EDIFICIO C", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textEC = tk.Text(pestana6, font=("Times New Roman", 14), bg="red",height = 16, width = 55)
texto5 ="""Áreas en planta baja:
Oficina Administrativa de control de laboratorios de Redes.
Áreas en planta alta:
Oficinas Académicas de Dirección de Programa Educativo
Ingeniería en Sistemas Computacionales, Dirección de Programa
Educativo Redes y Telecomunicaciones y cubículos de docentes.
Espacios en planta baja:
Sala isóptica, aula-auditorio, Laboratorios de telemática, de redes,
CONACyT y de cómputo, 8 aulas para impartición de clase
sanitarios para hombres y mujeres, y un sanitario para hombres y
uno para mujeres adecuado para personas con discapacidad.
Espacios en planta alta:
Laboratorio de cómputo, 8 aulas para impartición de clase,
sanitarios para hombres y mujeres, y un sanitario para hombres y
uno para mujeres adecuado para personas con discapacidad,
elevador."""
textEC.insert(tk.END, texto5)
textEC.configure(state = tk.DISABLED)
textEC.place(x=0,y=28)
contacto = Label (pestana6, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=200, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvEC = Canvas(pestana6, width=350, height=350, bg='white')
canvEC.place(x=520,y=28)
imgEC = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\edificioC.jpg")
imgEC = imgEC.resize((350,350))
imagEC = ImageTk.PhotoImage(imgEC)
canvEC.create_image(1,1,anchor=NW, image=imagEC)#20, 20, anchor=NW, image=img)

#PESTAÑACIDEA
titulo = Label(pestana7, text = "CIDEA", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textCI = tk.Text(pestana7, font=("Times New Roman", 14), bg="red",height = 14, width = 55)
texto6 ="""Áreas en planta baja:
Oficinas Administrativas del Programa Educativo de Ingeniería en
Tecnología Automotriz, Oficinas administrativas de Talleres y
Laboratorios Pesados, Oficina Brose.
Áreas en planta alta:
Oficinas Administrativas de la Dirección de Investigación y 
Posgrado, Dirección de Planeación, Órgano Interno de Control.
Espacios en planta baja:
Laboratorio de manufactura aditiva e ingeniería inversa, 4 aulas
para la impartición de clases, sanitarios para hombres y mujeres, y un sanitario para hombres y uno para mujeres adecuado para
personas con discapacidad.
Espacios en planta alta:
Sala de juntas de CIDEA, Sala de acuerdos CIDEA."""
textCI.insert(tk.END, texto6)
textCI.configure(state = tk.DISABLED)
textCI.place(x=0,y=28)
contacto = Label (pestana7, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=200, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvCI = Canvas(pestana7, width=350, height=350, bg='white')
canvCI.place(x=520,y=28)
imgCI = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\fcidea.jpg")
imgCI = imgCI.resize((350,350))
imagCI = ImageTk.PhotoImage(imgCI)
canvCI.create_image(1,1,anchor=NW, image=imagCI)#20, 20, anchor=NW, image=img)

#PESTAÑACAPTA
titulo = Label(pestana8, text = "CAPTA", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textCA = tk.Text(pestana8, font=("Times New Roman", 14), bg="red",height = 12, width = 55)
texto7 ="""Áreas en planta baja:
Aulas académicas.
Áreas de planta alta:
Aulas académicas
Espacios en planta baja:
7 aulas para impartir clases, sanitarios para hombres y mujeres, y un sanitario para hombres y uno para mujeres adecuado para
personas con discapacidad.
Espacios en planta alta:
7 aulas para impartir clases, oficina-almacén de talleres pesados,
sanitarios para hombres y mujeres, y un sanitario para hombres y
uno para mujeres adecuado para personas con discapacidad."""
textCA.insert(tk.END, texto7)
textCA.configure(state = tk.DISABLED)
textCA.place(x=0,y=28)
contacto = Label (pestana8, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=200, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvCA = Canvas(pestana8, width=350, height=350, bg='white')
canvCA.place(x=520,y=28)
imgCA = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\fcapta.jpg")
imgCA = imgCA.resize((350,350))
imagCA = ImageTk.PhotoImage(imgCA)
canvCA.create_image(1,1,anchor=NW, image=imagCA)#20, 20, anchor=NW, image=img)

#PESTAÑACAFETERIA
titulo = Label(pestana9, text = "LA KAFE", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textKF = tk.Text(pestana9, font=("Times New Roman", 14), bg="red",height = 8, width = 55)
texto8 ="""Áreas:
Oficinas administrativas del servicio de comedor.
Espacios en planta baja:
Cocina, cafetería, anexos de cafetería, OXXO, sanitarios para
hombres y mujeres, y un sanitario para hombres y uno para 
mujeres adecuado para personas con discapacidad.
Espacios en sótano:
Almacén general."""
textKF.insert(tk.END, texto8)
textKF.configure(state = tk.DISABLED)
textKF.place(x=0,y=28)
contacto = Label (pestana9, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=200, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvKF = Canvas(pestana9, width=350, height=350, bg='white')
canvKF.place(x=520,y=28)
imgKF = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\lakafe.jpg")
imgKF = imgKF.resize((350,350))
imagKF = ImageTk.PhotoImage(imgKF)
canvKF.create_image(1,1,anchor=NW, image=imagKF)#20, 20, anchor=NW, image=img)

#PESTAÑABIBLIOTECA
titulo = Label(pestana10, text = "BIBLIOTECA", bg = "red", fg = "blue", font = ("Arial",18)).place(x = 260,y = 0)

textBI = tk.Text(pestana10, font=("Times New Roman", 14), bg="red",height = 4, width = 55)
texto9 = """El edificio cuenta con la tienda UPQ, donde se puede adquirir 
mercancía de la universidad tanto como materiales de papelería, así mismo se encuentran Servicios Escolares, mientras que en la 
parte superior el espacio esta dedicado para aulas escolares."""
textBI.insert(tk.END, texto9)
textBI.configure(state = tk.DISABLED)
textBI.place(x=0,y=28)
contacto = Label (pestana10, text = "Contacto\nCarretera Estatal 420 SN, El Marqués Querétaro CP 76240\nTelefono: 101 9000\nrecepcion@upq.mx", bg = "blue", fg = "white", width=200, font=("Times New Roman", 10), justify = "left").place(x = -250,y = 440)

canvBI = Canvas(pestana10, width=350, height=350, bg='white')
canvBI.place(x=520,y=28)
imgBI = Image.open("C:\\Users\\jonat\\OneDrive\\Documentos\\UPQ\\5to cuatri\\UPQ Fundamentos de Programación Orientada a Objetos\\TRABAJOS\\P2\\FPOO184\\AvancePI\\bibliot.jpg")
imgBI = imgBI.resize((350,350))
imagBI = ImageTk.PhotoImage(imgBI)
canvBI.create_image(1,1,anchor=NW, image=imagBI)#20, 20, anchor=NW, image=img)

#PESTAÑAREGISTROUSUARIOS
titulo= Label(pestana1,text="Registra tu acceso UPQ", bg="red", fg="blue", font=("Arial",18)).pack()

varNom= tk.StringVar()
iblNom= Label(pestana1, text="Nombre(s): ", bg = "red").pack()
txtNom= Entry(pestana1, textvariable=varNom).pack()

varAP= tk.StringVar()
iblAP= Label(pestana1, text="Apellido Paterno: ", bg = "red").pack()
txtAP= Entry(pestana1, textvariable=varAP).pack()

varAM= tk.StringVar()
iblAM= Label(pestana1, text="Apellido Materno: ", bg = "red").pack()
txtAM= Entry(pestana1, textvariable=varAM).pack()

varED= tk.StringVar()
iblED= Label(pestana1, text="Edad: ", bg = "red").pack()
txtED= Entry(pestana1, textvariable=varED).pack()

varCor= tk.StringVar()
iblCor= Label(pestana1, text="Correo electronico: ", bg = "red").pack()
txtCor= Entry(pestana1, textvariable=varCor).pack()


btnGuardar= Button(pestana1, text="Registrarse",command=ejecutaInsert).pack()

#PESTAÑA1:Formulario de materiales
titulo = Label(pestana11, text = "Registro de Materiales", fg = "blue", font = ("Modern", 18)).pack()

varMat = tk.StringVar()
lblNom = Label(pestana11, text = "Nombre del material: ").pack()
txtNom = Entry(pestana11, textvariable = varMat).pack()

varCan = tk.StringVar()
lblCor = Label(pestana11, text = "Cantidad: ").pack()
txtCor = Entry(pestana11, textvariable = varCan).pack()

btnGuardar = Button(pestana11, text = "Guardar Material", command = ejecutaInsert2).pack()

#PESTAÑA2:Buscar material
titulo2 = Label(pestana12, text = "Buscar Material", fg = "red", font = ("Modern", 18)).pack()

varBusmat = tk.StringVar()
lblid = Label(pestana12, text = "Identificador de material: ").pack()
txtid = Entry(pestana12, textvariable = varBusmat).pack()

btnBusqueda = Button(pestana12, text = "Buscar", command = ejecutaSelect).pack()

subBus = Label(pestana12, text = "Registrado:", fg = "blue", font = ("Modern", 18)).pack()
textBus = tk.Text(pestana12, height = 5, width = 52)
textBus.pack()

#PESTAÑA3: Consultar materiales
titulo3 = Label(pestana13, text = "Consultar Materiales", fg = "red", font = ("Modern", 18)).pack()

btnConsulta = Button(pestana13, text = "Consulta", command = ejecutaConsulta).pack()

columns = ("id", "material", "cantidad")

tabla = ttk.Treeview(pestana13, columns = columns, show = "headings")

tabla.column("id", anchor=tk.W, width=50)
tabla.column("material", anchor=tk.W, width=150)
tabla.column("cantidad", anchor=tk.W, width=150)

tabla.heading("id", text = "ID", )
tabla.heading("material", text = "NOMBRE MATERIAL")
tabla.heading("cantidad", text = "CANTIDAD")

tabla.pack()

#PESTAÑA4:Actualizar material
titulo4 = Label(pestana14, text = "Actualizar Material", fg = "red", font = ("Modern", 18)).pack()

varIDmat = tk.StringVar()
varaMat = tk.StringVar()
varaCan = tk.StringVar()
lblid = Label(pestana14, text = "Identificador de material: ").pack()
txtid = Entry(pestana14, textvariable = varIDmat).pack()
lanNom = Label(pestana14, text = "Cambiar nombre de material: ").pack()
txNom = Entry(pestana14, textvariable = varaMat).pack()
lanCor = Label(pestana14, text = "Cantidad: ").pack()
txCor = Entry(pestana14, textvariable = varaCan).pack()

btnActuali = Button(pestana14, text = "Actualizar", command = ejecutaActualizar).pack()

#PESTAÑA5:Eliminar Cantidad
titulo4 = Label(pestana15, text = "Eliminar Cantidad", fg = "red", font = ("Modern", 18)).pack()

varID2 = tk.StringVar()
lblid = Label(pestana15, text = "Identificador de material: ").pack()
txtid = Entry(pestana15, textvariable = varID2).pack()

btnBusqueda = Button(pestana15, text = "Buscar", command = ejecutaBusqueda).pack()

subBus2 = Label(pestana15, text = "Registrado:", fg = "blue", font = ("Modern", 18)).pack()
textBus2 = tk.Text(pestana15, height = 2, width = 52)
textBus2.pack()

btnBusqueda = Button(pestana15, text = "eliminar", command = ejecutaEliminar).pack()

panel.add(pestana1, text = "Acceso usuarios")
panel.add(pestana2, text = "LT1")
panel.add(pestana3, text = "Talleres")
panel.add(pestana4, text = "Edificio A")
panel.add(pestana5, text = "Edificio B")
panel.add(pestana6, text = "Edificio C")
panel.add(pestana7, text = "CIDEA")
panel.add(pestana8, text = "CAPTA")
panel.add(pestana9, text = "Cafeteria")
panel.add(pestana10, text = "Biblioteca")

panel.add(pestana11, text = "Formulario de materiales")
panel.add(pestana12, text = "Buscar materiales")
panel.add(pestana13, text = "Consultar materiales")
panel.add(pestana14, text = "Actualizar materiales")
panel.add(pestana15,text = "Eliminar materiales")

ventana.mainloop()