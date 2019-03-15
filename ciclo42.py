#-*-coding:utf-8-*-

'''42. Determinar a cuánto es igual el promedio entero de los elementos de la serie de
Fibonacci entre 0 y 1000.'''

try:
	inicial = 0
	numero = 1
	ultimo = 0
	penultimo = 0
	suma = 0
	cont = 0
	prom = 0

	while numero <=1000:
		penultimo = ultimo
		ultimo = numero
		numero = penultimo + ultimo	
		suma = suma + ultimo
		cont+=1
	prom = suma /cont
	print "El promedio de los elementos de la serie Fibonacci entre 0 y 1000 es: %d"%prom


except ValueError:
	print "Error..."
