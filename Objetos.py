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

print("")
print("#### Objeto Heroe ####")
print("El personaje se llama: " + heroe.nombre)
print("pertenece a la especie: " + heroe.especie)
print("y tiene una altura de: " + str(heroe.altura))

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargaH)

print("")
print("#### Objeto Villano ####")
print("El personaje se llama: " + villano.nombre)
print("pertenece a la especie: " + villano.especie)
print("y tiene una altura de: " + str(villano.altura))

villano.correr(False)
villano.lanzarGranadas()
villano.recargarArma(recargaV)
