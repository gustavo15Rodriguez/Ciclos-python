#-*-coding:utf-8-*-

'''45. Leer un número y calcularle el factorial a todos los enteros comprendidos entre 1 y el
número leído.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))
	factorial = 1
	for i in range (1, numero+1):
		factorial = factorial * i

		print "El factorial del numero %d es: %d"%(i, factorial)

except ValueError:
	print "Error..."
