#Declaramos las variables 
cont=int(0)
mayor=int(0)
menor=int(1000)
total=int()
par=int()
impar=int()
factorial=int()
contfactorial=int(1)


#Creamos un bucle que entrar en él las 25 veces, para introducir los valores de los alumnos

while cont <=25:
	#Introducimos la edad de los alumno
	edad=int(input("Introduce la edad del alumno : "))
	total= total+edad
	#En primero lugar sacaremos el factorial de todas las edades 
	factorial=edad
	while contfactorial < edad:
		factorial = factorial * contfactorial
		contfactorial = contfactorial + 1
		print("El factorial de este numero es ",factorial)

	#Este bucle if se encargará de controlar que edad de las introducida es la menor de todas
	if edad < menor:
		menor=edad
		pass
#Este bulce se encargara de controlar cual de las edades introducidas es la mayor
	if edad > mayor:
		mayor = edad
		pass
#con este bucle controlaremos las edades pares e impares , en el primer caso si dividimos
#la edad entre dos y el resto es cero significa que la edad introducida es par 

	if edad%2==0:
		par+=1
	else :
		impar+=1
	contfactorial=edad
	cont+=1

#Ahora imprimimos todos los datos
	print("la edad menor es de ", menor)
	print("la edad  mayor es de : ", mayor)
	print("la  media es de ", total/cont)
	print("Hay ",par, "numeros pares " )
	print("Hay ",impar, "numeros impares " )