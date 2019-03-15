#-*-coding:utf-8-*-

'''44. Leer un número y calcularle su factorial.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))
	factorial = 1
	for i in range (numero):
		factorial = factorial * numero
		numero -=1

	print "El factorial del numero leido es: %d"%factorial 

except ValueError:
	print "Error..."
