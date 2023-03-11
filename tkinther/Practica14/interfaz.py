import tkinter as tk
from funciones import CajaPopular
from tkinter import messagebox

class Application (tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title("Caja popular")
        self.create_widgets()
        
    def create_widgets(self):
        self.label1 = tk.Label(self.master, text = "Numero de cuenta")
        self.label1.grid(row = 0, column = 0)
        self.num_cuenta_origen_entry = tk.Entry(self.master)
        self.num_cuenta_origen_entry.grid(row = 0, column = 1)
        
        self.label2 = tk.Label(self.master, text = "Titular")
        self.label2.grid(row = 1, column = 0)
        self.titular_entry = tk.Entry(self.master)
        self.titular_entry.grid(row = 1, column = 1)
        
        self.label3 = tk.Label(self.master, text = "Edad")
        self.label3.grid(row = 2, column = 0)
        self.edad_entry = tk.Entry(self.master)
        self.edad_entry.grid(row = 2, column = 1)
        
        self.label4 = tk.Label(self.master, text = "Saldo")
        self.label4.grid(row = 3, column = 0)
        self.saldo_entry = tk.Entry(self.master)
        self.saldo_entry.grid(row = 3, column = 1)
        
        self.agregar_btn = tk.Button(self.master, text = "Agregar cuenta", command = self.agregar_cuenta)
        self.agregar_btn.grid(row = 4, column = 0)
        
        self.consultar_btn = tk.Button(self.master, text = "Consultar saldo", command = self.consultar_saldo)
        self.consultar_btn.grid(row = 4, column = 1)
        
        self.ingresar_btn = tk.Button(self.master, text = "Ingresar efectivo", command = self.ingresar_efectivo)
        self.ingresar_btn.grid(row = 5, column = 0)
        
        self.retirar_btn = tk.Button(self.master, text = "Retirar efectivo", command = self.retirar_efectivo)
        self.retirar_btn.grid(row = 5, column = 1)
        
        self.depositar_btn = tk.Button(self.master, text = "Depositar a otra cuenta", command = self.depositar_a_otra_cuenta)
        self.depositar_btn.grid(row = 7, column = 0)
        
        self.label5 = tk.Label(self.master, text = "Número de cuenta origen:")
        self.label5.grid(row = 6, column = 0)
        self.num_cuenta_origen = tk.Entry(self.master)
        self.num_cuenta_origen.grid(row = 6, column = 1)
        
        self.label6 = tk.Label(self.master, text = "Número de cuenta destino:")
        self.label6.grid(row = 7, column = 0)
        self.num_cuenta_destino = tk.Entry(self.master)
        self.num_cuenta_destino.grid(row = 7, column = 1)

        self.label7 = tk.Label(self.master, text = "Cantidad:")
        self.label7.grid(row = 8, column = 0)
        self.cantidad = tk.Entry(self.master)
        self.cantidad.grid(row = 8, column = 1)

        
        self.quit_button = tk.Button(self.master, text = "Salir", command= self.master.quit)
        self.quit_button.grid(row=9, column=1)
        
        self.caja_popular = CajaPopular()

        
    def agregar_cuenta(self):
        num_cuenta_origen = self.num_cuenta_origen_entry.get()
        titular = self.titular_entry.get()
        edad = self.edad_entry.get()
        saldo = self.saldo_entry.get()
        self.caja_popular.agregar_cuenta(num_cuenta_origen, titular, edad, saldo)
    
    def consultar_saldo(self):
        num_cuenta_origen = self.num_cuenta_origen_entry.get()
        saldo = self.caja_popular.consultar_saldo(num_cuenta_origen)
        if saldo is None:
            tk.messagebox.showerror("Error", "No se encontró la cuenta")
        else:
            tk.messagebox.showinfo("Saldo", f"El saldo es: {saldo}")
            
    def ingresar_efectivo(self):
        num_cuenta_origen = self.num_cuenta_origen_entry.get()
        cantidad = self.saldo_entry.get()
        if self.caja_popular.ingresar_efectivo(num_cuenta_origen, cantidad):
            tk.messagebox.showinfo("Éxito", "Se ha ingresado efectivo a la cuenta")
        else:
            tk.messagebox.showerror("Error", "No se encontró la cuenta o la cantidad es inválida")
    
    def retirar_efectivo(self):
        num_cuenta_origen = int(self.num_cuenta_origen.get())
        cantidad = float(self.cantidad.get())
        resultado = self.caja_popular.retirar_efectivo(num_cuenta_origen, cantidad)
        if resultado:
            tk.messagebox.showinfo("Retirar efectivo", "El retiro se ha realizado con éxito.")
        else:
            tk.messagebox.showerror("Retirar efectivo", "No se puede retirar esa cantidad de la cuenta especificada.")

    def depositar_a_otra_cuenta(self):
        num_cuenta_origen = int(self.num_cuenta_origen.get())
        num_cuenta_destino = int(self.num_cuenta_destino.get())
        cantidad = float(self.cantidad.get())
        resultado = self.caja_popular.depositar_a_otra_cuenta(num_cuenta_origen, num_cuenta_destino, cantidad)
        if resultado:
            tk.messagebox.showinfo("Depositar a otra cuenta", "El depósito se ha realizado con éxito.")
        else:
            tk.messagebox.showerror("Depositar a otra cuenta", "No se puede depositar esa cantidad de la cuenta origen o destino especificadas.")
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()








