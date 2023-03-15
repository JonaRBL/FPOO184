import random
from datetime import datetime
class Matricula:
    def __init__(self, nom, apellpa, apellma, anna, carr):
        self.nombre = nom
        self.apellidopaterno = apellpa
        self.apellidomaterno = apellma
        self.anonacimiento = anna
        self.carrera = carr
    
    def genmat(self):
        anoActu = datetime.now().year
        anoActu = str(anoActu)[-2:]
        anonac = str(self.anonacimiento)[-2:]
        letrasApellidos = self.apellidomaterno[:3] + self.apellidopaterno[:3]
        letraNombre = self.nombre[0]
        letrasCarrera = self.carrera[:3]
        digitosAleatorios = str(random.randint(100, 999))
        matricula = letrasCarrera + anoActu + anonac + letraNombre + letrasApellidos + digitosAleatorios
        return matricula
    
    ''''''