#-*-coding:utf-8-*-

'''46. Leer un número entero y calcular el promedio entero de los factoriales de los enteros
comprendidos entre 1 y el número leído.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	factorial = 1
	cont = 0
	prom = 0
	for i in range(1, numero+1):
		factorial = factorial * i
		cont += 1

		prom = factorial / cont

	print prom

except ValueError:
	print "Error..."
