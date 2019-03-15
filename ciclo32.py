#-*-coding:utf-8-*-

'''32. Leer números hasta que digiten 0 y determinar a cuanto es igual el promedio entero de
los número primos leídos.'''

try:
	numero = 1
	cont = 0
	cont2=0
	suma = 0
	prom = 0

	while numero != 0:
		numero = int(raw_input("Digite el primer numero: "))

		cont= 0
		
		for i in range(1,numero+1):

			
			if numero%i==0:
				cont+=1

		if cont == 2:
			suma+=numero
			cont2+=1

	
	if suma == 0:
		print "No se ingresaron numeros primos"

	else:

		prom = suma / cont2
		print "El promedio de los numeros primos es igual a: %d"%prom


	
except ValueError:
	print "Error..."	
