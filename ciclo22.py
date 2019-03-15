#-*-coding:utf-8-*-

'''22. Leer un número entero y determinar cuántas veces tiene el dígito 1.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))
	cont = 0

	while numero > 0:
		digito = numero % 10
		numero = numero / 10


		if digito == 1:
			cont += 1

	print "El numero ingresado posee %d"%cont + " veces el digito 1."



except ValueError:
	print "Error..."	