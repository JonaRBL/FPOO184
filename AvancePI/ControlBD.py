from tkinter import messagebox
import sqlite3


class controladorBD:
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("D:/canel/Documents/GitHub/POOAURL/ProyectoInt/RegistroUPQ.db")
            print("Conectado BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    #Metodo para Insertar
    def guardarUsuario(self,nom,ap,am,ed,cor):
        conx=self.conexionBD()
        
        if(nom == "" or ap == "" or am == "" or ed == "" or cor ==""):
            messagebox.showwarning("Acceso Denegado", "Rellena todos los registros")
            conx.close()
        else:
            cursor = conx.cursor()
            datos=(nom,ap,am,ed,cor)
            qrInsert= "insert into Ingresados(Nombre,Apellido_Paterno,Apellido_Materno,Edad,Correo) values(?,?,?,?,?)"
            
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Se Registro tu acceso")
            