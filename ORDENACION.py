#EJERCICIO ORDENACION 
# Por MIGUEL ANGEL RODRIGUEZ FLORES
contador2=int(0)

def listaaleatoria() :
# Para importar la biblioteca random al completo
	import random
	# Para importar sólo determinadas funciones (randrange y choice)
	from random import randrange, choice
	# Declaro las variables 
	posicion=int(0)
	lista1=[]
	contadorlista=int(0)
	contador=int(0)
	
		
	##bucle para crear nmumeros e introducirlos en la lista1 
	while contador <= 6 :
		numeroaleatorio=random.randint(0,99)
		##crea los numeros aleatorios y los mete en lista1 	
		lista1.append(numeroaleatorio)
		contador=contador+1

	#ordena la lista de numeros aleatorios por orden ascendente	
	for recorrido in range (1,len(lista1)) :
			for posicion in range(len(lista1) - recorrido):
				if lista1[posicion] > lista1[posicion + 1]:
					temp = lista1[posicion]
					lista1[posicion] = lista1[posicion + 1]
					lista1[posicion + 1] = temp

	contadorlista=contadorlista+1
	print(lista1)

#creo un bucle llamando 7 veces a la funcion que crea una lista de numeros aleatorios
while contador2 <= 6:
	listaaleatoria()
	contador2=contador2+1