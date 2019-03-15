#-*-coding:utf-8-*-

'''24. Leer un número entero y determinar a cuánto es igual la suma de sus dígitos pares.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	suma = 0

	while numero > 0:
		digito = numero % 10
		numero = numero / 10
		if digito % 2 == 0:
			suma += digito

	if suma == 0:
		print "Ninguno de los digitos del numero ingresado es par."

	else:
		print "La suma de los digitos pares es %d"%suma

except ValueError:
	print "Error..."