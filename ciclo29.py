#-*-coding:utf-8-*-

'''29. Leer un número entero y determinar a cuánto es igual el primero de sus dígitos.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))
	cont = 0

	while numero > 0:
		for i in range(cont):
			digito = numero % 10
		numero = numero / 10
		cont+=1

	print "El primer digito del numero ingresado es: %d"%digito

	
except ValueError:
	print "Error..."	