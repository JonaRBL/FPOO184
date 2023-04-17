from tkinter import messagebox
import sqlite3


class controladorBD:
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("C:/Users/jonat/OneDrive/Documentos/UPQ/5to cuatri/UPQ Fundamentos de Programación Orientada a Objetos/TRABAJOS/P2/FPOO184/AvancePI/RegistroUPQ.db")
            print("Conectado BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    def conexionBD2(self):
        try:
            conexion=sqlite3.connect("C:/Users/jonat/OneDrive/Documentos/UPQ/5to cuatri/UPQ Fundamentos de Programación Orientada a Objetos/TRABAJOS/P2/FPOO184/AvancePI/InventarioUPQ.db")
            print("Conectado BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    #Metodo para Insertar usuarios
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
    
     #Metodo para insertar material
    def guardarMaterial(self, mate, cant):
        
        #1. llamar a la conexion
        conx = self.conexionBD2()
        
        #2. Revisar parametros vacios
        if(mate == "" or cant == ""):
           messagebox.showwarning("Cuidado!", "Ningún campo puede estar vacio")
           conx.close() 
        else:
            #3. Preparar los datos y el querySQL
            cursor = conx.cursor()
            datos = (mate, cant)
            qrInsert = "insert into TBMateriales(Material, Cantidad) values(?,?)"
            
            #4. Proceder a insertar y cerramos la conx
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito!!", "Se guardo el material")
    
    def consultaMaterial(self, id):
        #1. preparar la conexion
        conx = self.conexionBD2()
        
        #2. verificar que el ID no este vacio
        if (id == ""):
            messagebox.showwarning("Cuidado", "ID vacio, escribe uno valido")
            conx.close()
        else:
            #3. proceder a buscar el usuario
            try:
                #4. prepara lo necesario para el select
                cursor = conx.cursor()
                sqlSelect = "select * from TBMateriales where IDmaterial =" + id
                
                #5. ejecucion y guardado de la consulta
                cursor.execute(sqlSelect)
                RSmaterial = cursor.fetchall()
                conx.close()
                
                return RSmaterial
            
            except sqlite3.OperationalError:
                print("Error de Consulta")
    
    def consultasMateriales(self):
        conx = self.conexionBD2()
        
        cursor = conx.cursor()
        sqlConsulta = "select * from TBMateriales"
        
        cursor.execute(sqlConsulta)
        registros = cursor.fetchall()
        conx.close()
        
        return registros
    
    def actualizarMaterial(self, id, matent, cantent):
        conx = self.conexionBD2()
        
        if(id == "" or matent == "" or cantent == ""):
            messagebox.showwarning("Cuidado", "ningun campo puede estar vacio")
            conx.close()
        else:
            try:
                cursor = conx.cursor()
                mate = matent
                cant = cantent
                sqlActuali = "UPDATE TBMateriales SET Material=?, Cantidad=? WHERE IDmaterial=?"
                
                cursor.execute(sqlActuali, [mate, cant, id])
                usuAct = cursor.fetchall()
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito!!", "Datos actualizados")
                #noment.delete(0, tk.END)
                #corent.delete(0, tk.END)
                #conent.delete(0, tk.END)
                
                return usuAct
            
            except sqlite3.OperationalError:
                print("Error de Consulta")
    
    def eliminarMaterial(self, id):
        conx = self.conexionBD2()
        
        if(id == ""):
            messagebox.showwarning("Cuidado", "ningun campo puede estar vacio")
            conx.close()
        else:
            try:
                cursor = conx.cursor()
                sqlDelete = "DELETE FROM TBMateriales WHERE IDmaterial=?"
                
                cursor.execute(sqlDelete, [id])
                usuEli = cursor.fetchall()
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito!!", "Material eliminado")
                #noment.delete(0, tk.END)
                #corent.delete(0, tk.END)
                #conent.delete(0, tk.END)
                
                return usuEli
            
            except sqlite3.OperationalError:
                print("Error de Consulta")
            