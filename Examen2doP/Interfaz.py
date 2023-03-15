from tkinter import *
from tkinter import messagebox
from generador import Matricula

ventana = Tk()
ventana.title("Matricula")
ventana.geometry("600x400")
ventana.config(bg="blue")



nombre = Label(ventana, text="Ingrese su nombre")
nombre.grid(row=0,column=0)
nom = Entry(ventana)
nom.grid(row=0,column=1)

apellidoPa = Label(ventana, text="Ingrese su apellido paterno:")
apellidoPa.grid(row=1,column=0)
apPa = Entry(ventana)
apPa.grid(row=1,column=1)

apellidoMa = Label(ventana, text="Ingrese su apellido materno:")
apellidoMa.grid(row=2,column=0)
apMa = Entry(ventana)
apMa.grid(row=2,column=1)

anoNacimiento = Label(ventana, text="Ingrese su año de nacimiento:")
anoNacimiento.grid(row=3,column=0)
anNa = Entry(ventana)
anNa.grid(row=3,column=1)

carrera = Label(ventana, text="Ingrese la carrera que esta cursando:")
carrera.grid(row=4,column=0)
carr = Entry(ventana)
carr.grid(row=4,column=1)

#matri = Matricula(nom, apPa, apMa, anNa, carr)
    
def genemat():
    entrynom = nom.get()
    entryapellipa =  apPa.get()
    entryapellima = apMa.get()
    entryanona = anNa.get()
    entrycarrera = carr.get()
    matri = Matricula(entrynom, entryapellipa, entryapellima, entryanona, entrycarrera)
    matri.genmat()   
    
generamat = Button(ventana, text="Generar matricula", bg="yellow", command = genemat)
generamat.grid(row=5,column=0)


ventana.mainloop()

