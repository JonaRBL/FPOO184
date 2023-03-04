class acceso():
    Nusu = 0
    def __init__(self,contrasena,correo):
        self.contrasena = contrasena
        self.correo = correo
        
        self.conecta = False
        self.inten = 3
        
        acceso.Nusu += 1
        
    def conect (self, passw = None):
        if passw == None:
            contra = input("Ingresa tu contraseña: ")
        else:
            contra = passw
        if contra == self.contrasena:
            print("Se accedio con exito !!")
            self.conecta = True
            return True
        else:
            self.inten -= 1
            if self.inten > 0:
                print("Contraseña incorrecta, Revisa tus credenciales")
                if passw != None:
                    return False
                print("Intentos restantes", self.inten)
                self.conect()
            else:
                print("Error, no se pudo acceder")
    
    def __str__ (self):
        if self.conecta:
            con = "Conectado"
        else:
            con = "Desconectado"
        return f"El correo del usuario es {self.correo} y esta {con}"