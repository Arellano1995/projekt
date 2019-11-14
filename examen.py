#!/usr/bin/python

# -*- coding: utf-8 -*-

import os

def menu():

	"""

	Función que limpia la pantalla y muestra nuevamente el menu

	"""

	os.system('cls') # NOTA para windows tienes que cambiar clear por cls

	print ("Selecciona una opción")

	print ("\t1 - primera opción")

	print ("\t2 - segunda opción")

	print ("\t3 - tercera opción")

	print ("\t9 - salir")


while True:

	# Mostramos el menu

	menu()

	# solicituamos una opción al usuario

	opcionMenu = input("\ninserta un numero valor >> ")

	if opcionMenu=="1":

		print ()
        
		input("Has pulsado la opción 1...\n\npulsa una tecla para continuar")


	elif opcionMenu=="2":

		print ("")

		input("Has pulsado la opción 2...\n\npulsa una tecla para continuar")

	elif opcionMenu=="3":

		print ("")

		input("Has pulsado la opción 3...\n\npulsa una tecla para continuar")

	elif opcionMenu=="9":

		break

	else:

		print ("")

		input("No has pulsado ninguna opción correcta...\n\npulsa una tecla para continuar")