#-*-coding:utf-8-*-

'''2.Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	for i in range (1,numero+1):
		if i%2 == 0:
			print i

except ValueError:
	print "Error..."
