#-*-coding:utf-8-*-

'''39. Se define la serie de Fibonacci como la serie que comienza con los dígitos 1 y 0 y va
sumando progresivamente los dos últimos elementos de la serie, así:
 
0    1    1    2    3    5    8    13    21    34.......

Utilizando el concepto de ciclo generar la serie de Fibonacci hasta llegar o sobrepasas el
número 10000.'''

try:
	inicial = 0
	numero = 1
	ultimo = 0
	penultimo = 0
	
	print inicial
	print numero

	for i in range (0,20):
		penultimo = ultimo
		ultimo = numero
		numero = penultimo + ultimo	
		print numero

except ValueError:
	print "Error..."

