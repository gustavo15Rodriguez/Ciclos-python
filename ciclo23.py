#-*-coding:utf-8-*-

'''23. Leer un número entero y determinar si la suma de sus dígitos es también un número
primo.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	suma = 0
	cont = 0

	while numero > 0:
		digito = numero % 10
		suma = suma + digito
		numero = numero / 10

	print suma	


	for i in range (1, suma+1):
		if suma % i == 0:
			cont += 1

	if suma == 1:
		print "La suma de los digitos del numero ingresado no origina un numero primo "

	elif cont != 2:
		print "La suma de los digitos del numero ingresado no origina un numero primo "

	else:
		print "La suma de los digitos del numero ingresado si origina un numero primo que es %d"%suma

except ValueError:
	print "Error..."	