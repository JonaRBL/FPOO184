from tkinter import *
import random
import string


lonc = 8
class generCon():
    def __init__(self,pedirLongi,botonNegro,boton2):
        self.botonNegro = botonNegro
        self.boton2 = boton2
        self.pedirLongi = pedirLongi
        self.password = ""
        
    def generarContra(self):
        self.pedirLongi = int(self.pedirLongi.get())
        self.botonNegro = bool(self.botonNegro.get())
        self.boton2 = bool(self.boton2.get())
            
        caractPerm = string.ascii_lowercase
        if self.botonNegro:
            caractPerm += string.ascii_uppercase
        if self.boton2:
            caractPerm += string.punctuation
                
        contrasena = "".join(random.choice(caractPerm) for i in range(self.pedirLongi))
        self.password = contrasena
        return contrasena
        #contrasenaGenerada.config(text = contrasena)
        
    def fortalezaContra(self):
        #contrasena = contrasenaGenerada.cget("text")
        contrasena = self.password    
        has_uppercase = any(c.isupper() for c in contrasena)
        has_lowercase = any(c.islower() for c in contrasena)
        has_digit = any(c.isdigit() for c in contrasena)
        has_especial = any(c in string.punctuation for c in contrasena)
            
        testo = "Débil"
        if has_uppercase and has_lowercase and has_digit and has_especial:
            testo = "Fuerte"
        elif (has_uppercase and has_lowercase and has_digit) or (has_lowercase and has_digit and has_especial):
            testo = "Moderada"
            
        testo_message = f"La fortaleza de la contraseña es: {testo}"
        self.password_label.config(text=testo_message)

