class Cuenta:
    def __init__(self, num_cuenta_origen, titular, edad, saldo):
        self.num_cuenta_origen = num_cuenta_origen
        self.titular = titular
        self.edad = edad
        self.saldo = saldo

class CajaPopular:
    def __init__(self):
        self.cuentas = []
    
    def agregar_cuenta(self, num_cuenta_origen, titular, edad, saldo):
        self.cuentas.append(Cuenta(num_cuenta_origen, titular, edad, saldo))
    
    def consultar_saldo(self, num_cuenta_origen):
        for cuenta in self.cuentas:
            if cuenta.num_cuenta_origen == num_cuenta_origen:
                return cuenta.saldo
        return None
    
    def ingresar_efectivo(self, num_cuenta_origen, cantidad):
        for cuenta in self.cuentas:
            if cuenta.num_cuenta_origen == num_cuenta_origen:
                cuenta.saldo += cantidad
                return True
        return False
    
    def retirar_efectivo(self, num_cuenta_origen, cantidad):
        for cuenta in self.cuentas:
            if cuenta.num_cuenta_origen == num_cuenta_origen:
                if cuenta.saldo >= cantidad:
                    cuenta.saldo -= cantidad
                    return True
                else:
                    return False
        return False
    
    def depositar_a_otra_cuenta(self, num_cuenta_origen, num_cuenta_destino, cantidad):
        for cuenta_origen in self.cuentas:
            if cuenta_origen.num_cuenta_origen == num_cuenta_origen:
                for cuenta_destino in self.cuentas:
                    if cuenta_destino.num_cuenta_origen == num_cuenta_destino:
                        if cuenta_origen.saldo >= cantidad:
                            cuenta_origen.saldo -= cantidad
                            cuenta_destino.saldo += cantidad
                            return True
                        else:
                            return False
        return False