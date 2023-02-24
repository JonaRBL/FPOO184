from Personaje import *

#1. Solicitar datos
print("")
print("#### Datos Heroe ####")
especieH = input("escribe la especie del Heroe: ")
nombreH = input("escribe el nombre del Heroe: ")
alturaH = float(input("escribe la altura del Heroe: "))
recargaH = int(input("Cuantas balas recargas al heroe: "))

print("")
print("#### Datos Villano ####")
especieV = input("escribe la especie del Villano: ")
nombreV = input("escribe el nombre del Villano: ")
alturaV = float(input("escribe la altura del Villano: "))
recargaV = int(input("Cuantas balas recargas al Villano: "))

#2. Crear objeto de la clase personaje

heroe = Personaje(especieH, nombreH, alturaH)
villano = Personaje(especieV, nombreV, alturaV)


#3. Usar atributos y metodos

#ejemplo del set para 1 atributo
heroe.setNombre(" Viajero ")

print("")
print("#### Objeto Heroe ####")
print("El personaje se llama: " + heroe.getNombre())
print("pertenece a la especie: " + heroe.getEspecie())
print("y tiene una altura de: " + str(heroe.getAltura()))

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargaH)

#ejemplo de un metodo privado
heroe.__pensar()

print("")
print("#### Objeto Villano ####")
print("El personaje se llama: " + villano.getNombre())
print("pertenece a la especie: " + villano.getEspecie())
print("y tiene una altura de: " + str(villano.getAltura()))

villano.correr(False)
villano.lanzarGranadas()
villano.recargarArma(recargaV) 
