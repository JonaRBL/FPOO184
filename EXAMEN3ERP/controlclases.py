from tkinter import messagebox
import sqlite3

class controlaBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        
        try:
            conexion = sqlite3.connect("C:/Users/jonat/OneDrive/Documentos/UPQ/5to cuatri/UPQ Fundamentos de Programación Orientada a Objetos/TRABAJOS/P2/FPOO184/EXAMEN3ERP/BD_Banco.db")
            print("Conectado a la base de datos")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar a la BD")
    
    def guardarCuenta(self, cuen, sala):
    
        conx = self.conexionBD()
        
        if(cuen == "" or sala == ""):
           messagebox.showwarning("Cuidado!", "Ningún campo puede estar vacio")
           conx.close() 
        else:
            cursor = conx.cursor()
            datos = (cuen, sala)
            qrInsert = "insert into TBCuentas (NoCuenta, Saldo) values(?,?)"
            
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito!!", "Se guardo la cuenta")
    
    def consultaCuenta(self, id):
        conx = self.conexionBD()
        
        if (id == ""):
            messagebox.showwarning("Cuidado", "ID vacio, escribe uno valido")
            conx.close()
        else:
            try:
                cursor = conx.cursor()
                sqlSelect = "select * from TBCuentas where IDCuenta =" + id
                
                cursor.execute(sqlSelect)
                RScuenta = cursor.fetchall()
                conx.close()
                
                return RScuenta
            
            except sqlite3.OperationalError:
                print("Error de Consulta")
    
    def consultasCuentas(self):
        conx = self.conexionBD()
        
        cursor = conx.cursor()
        sqlConsulta = "select * from TBCuentas"
        
        cursor.execute(sqlConsulta)
        registros = cursor.fetchall()
        conx.close()
        
        return registros
    
    def actualizarCuenta(self, id, cuent, salent):
        conx = self.conexionBD()
        
        if(id == "" or cuent == "" or salent == ""):
            messagebox.showwarning("Cuidado", "ningun campo puede estar vacio")
            conx.close()
        else:
            try:
                cursor = conx.cursor()
                cue = cuent
                sal = salent
                sqlActuali = "UPDATE TBCuentas SET NoCuenta=?, Saldo=? WHERE IDCuenta=?"
                
                cursor.execute(sqlActuali, [cue, sal, id])
                cuentaAct = cursor.fetchall()
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito!!", "Datos de la cuenta actualizados")
                #noment.delete(0, tk.END)
                #corent.delete(0, tk.END)
                #conent.delete(0, tk.END)
                
                return cuentaAct
            
            except sqlite3.OperationalError:
                print("Error de Consulta")
