from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    #preparamos la conexión a la BD para cuando sea necesario usarla
    def conexionBD(self):
        
        try:
            conexion = sqlite3.connect("C:/Users/jonat/OneDrive/Documentos/UPQ/5to cuatri/UPQ Fundamentos de Programación Orientada a Objetos/TRABAJOS/P2/FPOO184/tkinterSqlite/DBUsuarios.db")
            print("Conectado a la base de datos")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar a la BD")
    
    #Metodo para insertar
    def guardarUsuario(self, nom, cor, con):
        
        #1. llamar a la conexion
        conx = self.conexionBD()
        
        #2. Revisar parametros vacios
        if(nom == "" or cor == "" or con == ""):
           messagebox.showwarning("Cuidado!", "Ningún campo puede estar vacio")
           conx.close() 
        else:
            #3. Preparar los datos y el querySQL
            cursor = conx.cursor()
            conH = self.encriptarCont(con)
            datos = (nom, cor, conH)
            qrInsert = "insert into TBRegistros(nombre, correo, contra) values(?,?,?)"
            
            #4. Proceder a insertar y cerramos la conx
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito!!", "Se guardo el usuario")
    
    def encriptarCont(self,con):
        conPlana = con
        conPlana = conPlana.encode() #convierte la contraseña a bytes
        sal = bcrypt.gensalt()
        conHa = bcrypt.hashpw(conPlana, sal)
        print(conHa)
        return conHa
    
    def consultaUsuario(self, id):
        #1. preparar la conexion
        conx = self.conexionBD()
        
        #2. verificar que el ID no este vacio
        if (id == ""):
            messagebox.showwarning("Cuidado", "ID vacio, escribe uno valido")
            conx.close()
        else:
            #3. proceder a buscar el usuario
            try:
                #4. prepara lo necesario para el select
                cursor = conx.cursor()
                sqlSelect = "select * from TBRegistros where id =" + id
                
                #5. ejecucion y guardado de la consulta
                cursor.execute(sqlSelect)
                RSusuario = cursor.fetchall()
                conx.close()
                
                return RSusuario
            
            except sqlite3.OperationalError:
                print("Error de Consulta")