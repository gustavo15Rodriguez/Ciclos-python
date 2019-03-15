#-*-coding:utf-8-*-

'''Leer un número entero y determinar a cuánto es igual la suma de todos los enteros
comprendidos entre 1 y el número leído.'''

try:
	n = int(raw_input("Digite el numero deseado, positivo:"))

	suma = 0

	for i in range (1, n+1):
		suma = suma + i
		
	print "La suma de los numeros comprendidos entre 1 y %d"%n + " es igual a: %d"%suma	


except ValueError:
	print "Error..."
