#-*-coding:utf-8-*-

'''47. Leer un número entero y calcular a cuánto es igual la sumatoria de todos los factoriales
de los números comprendidos entre 1 y el número leído.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))
	factorial = 1
	suma = 0

	for i in range (1, numero+1):
		factorial = factorial * i
		suma = suma + factorial

	print "La sumatoria dee todos los fatoriales de los numeros de 1 a %d  es: %d" %(numero, suma)



except ValueError:
	print "Error..."
