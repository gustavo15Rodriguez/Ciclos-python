#-*-coding:utf-8-*-

'''6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y
cada uno de los dígitos.'''

try:
	n = int(raw_input("Digite un numero de tres digitos: "))

	if n>99 and n<=999:
		d1 = n / 100
		d2 = (n/10)%10
		d3 = n%10

	else:
		print "El numero ingresado debe poseer tres digitos."


	print "Enteros comprendidos entre 1 y %d"%d1

	for i in range (1, d1+1):
		print i		

	print "Enteros comprendidos entre 1 y %d"%d2

	for j in range (1, d2+1):
		print j	

	print "Enteros comprendidos entre 1 y %d"%d3


	for k in range (1, d3+1):
		print k	
	

except ValueError:
	print "Error..."
