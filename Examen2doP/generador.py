import random
from tkinter import messagebox
class Matricula:
    def __init__(self, nom, apellpa, apellma, anna, carr):
        self.nombre = nom
        self.apellidopaterno = apellpa
        self.apellidomaterno = apellma
        self.anonacimiento = anna
        self.carrera = carr
    
    def genmat(self):
        anoActu = str(2023)
        anoActu = str(anoActu)[-2:]
        anonac = str(self.anonacimiento)[-2:]
        letrasApellidos = str(self.apellidopaterno)[:3] + str(self.apellidomaterno)[:3]
        letraNombre = str(self.nombre)[0]
        letrasCarrera = str(self.carrera)[:3]
        digitosAleatorios = str(random.randint(100, 999))
        matricula = str(letrasCarrera) + str(anoActu) + str(anonac) + str(letraNombre) + str(letrasApellidos) + str(digitosAleatorios)
        msg = messagebox.showinfo("Generada", str(matricula))