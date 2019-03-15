#-*-coding:utf-8-*-

'''36. Mostrar en pantalla la tabla de multiplicar del número 5.'''

try:
	for i in range (1, 10+1):
		multiplicar = 5 * i
		print "5 * %d"%i + ": %d"%multiplicar
	
except ValueError:
	print "Error..."
