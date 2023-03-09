from interfaz import *
class generarCon():
    lonc = 8
    def __init__(self,contralong,mayuscula,espcaract):
        self.mayuscula = mayuscula
        self.espcaract = espcaract
        self.contralong = contralong
    
    def generarcontra(self):
        self.contralong = int(pedirLongi.get())
        self.mayuscula = bool(botonNegro.get())
        self.espcaract = bool(boton2.get())
        
        caractPerm = string.ascii_lowercase
        if self.mayuscula:
            caractPerm += string.ascii_uppercase
        if self.espcaract:
            caractPerm += string.punctuation
            
        contrasena = "".join(random.choice(caractPerm) for i in range(self.contralong))
        
        contrasenaGenerada.config(text = contrasena)
    
    def fortalezaContra(self):
        contrasena = contrasenaGenerada.cget("text")
        
        has_uppercase = any(c.isupper() for c in contrasena)
        has_lowercase = any(c.islower() for c in contrasena)
        has_digit = any(c.isdigit() for c in contrasena)
        has_especial = any(c in string.punctuation for c in contrasena)