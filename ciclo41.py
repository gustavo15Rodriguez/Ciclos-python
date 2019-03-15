#-*-coding:utf-8-*-

'''41. Determinar a cuánto es igual la suma de los elementos de la serie de Fibonacci entre 0 y
100.'''

try:
	inicial = 0
	numero = 1
	ultimo = 0
	penultimo = 0
	suma = 0

	while numero <=100:
		penultimo = ultimo
		ultimo = numero
		numero = penultimo + ultimo	
		suma = suma + ultimo
	print "La suma de los elementos de la serie Fibonacci es: %d"%suma


except ValueError:
	print "Error..."
