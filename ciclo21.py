#-*-coding:utf-8-*-

'''21. Leer un número entero y determinar a cuánto es igual la suma de sus dígitos.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	suma = 0

	while numero > 0:
		digito = numero % 10
		suma = suma + digito
		numero = numero / 10

	print "La suma de los digitos del numero ingresado es igual a: %d"%suma

except ValueError:
	print "Error..."