#-*-coding:utf-8-*-

'''38. Leer un número entero y mostrar en pantalla su tabla 
de multiplicar.'''

try:
	numero = int(raw_input("Digite el primer numero deseado: "))

	for i in range (1, 10+1):
		multiplicar = numero * i
		print "%d"%numero + " * %d"%i + " = %d"%multiplicar
	
except ValueError:
	print "Error..."

