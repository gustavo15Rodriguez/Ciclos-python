#-*-coding:utf-8-*-

'''20. Leer un número entero y determinar cuántos dígitos tiene.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	ind = 0

	while numero > 0:
		numero = numero / 10
		ind = ind +1
	print "El numero ingresado  tiene %d"%ind + " digitos"		
			

except ValueError:
	print "Error..."	