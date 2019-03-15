#-*-coding:utf-8-*-

'''43. Determinar cuántos elementos de la serie de Fibonacci se encuentran entre 1000 y 2000.'''

try:
	inicial = 0
	numero = 1
	ultimo = 0
	penultimo = 0
	cont = 0

	for i in range (0,2001):
		penultimo = ultimo
		ultimo = numero
		numero = penultimo + ultimo	

		if numero > 987 and numero <2001:
			cont +=1
		ultimo = numero
		numero = penultimo
	print "El numero de elementos de la serie Fibonacci entre 1000 y 2000 es: %d"%cont

except ValueError:
	print "Error..."
