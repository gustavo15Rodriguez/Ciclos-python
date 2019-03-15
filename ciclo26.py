#-*-coding:utf-8-*-

'''26.	Leer un número entero y determinar cuál es el mayor de sus dígitos. '''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	mayor = 0
	
	while numero > 0:
		digito = numero % 10
		numero = numero / 10

		if mayor < digito:
			mayor = digito
	print "El mayor digito del numero ingresado es: %d"%mayor

except ValueError:
	print "Error..."	