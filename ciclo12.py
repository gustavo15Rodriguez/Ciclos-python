#-*-coding:utf-8-*-

'''12. Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.'''

try:
	n = int(raw_input("Digite el primer numero de tres digitos:"))

	if n > 99 and n <=999:
		d1 = n/100
		d2 = (n/10) % 10
		d3 = n % 10
		cont = 0

		while d1 == 1 or d2 == 1 or d3 == 1:
			print "El numero %d"%n + " si posee el digito 1."
			cont+=1
			break

		if cont == 0:
			print "El numero ingresado no posee el digito 1."

	else:
		print "El numero ingresado debe poseer tres digitos."	



except ValueError:
	print "Error..."
