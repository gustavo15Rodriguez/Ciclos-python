#-*-coding:utf-8-*-

'''28.	Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos primos. '''

try:
	n1 = int(raw_input("Digite el primer numero: "))
	n2 = int(raw_input("Digite el segundo numero: "))

	cont1 = 0
	cont2 = 0

	while n1 > 0:
		digito = n1 % 10
		n1 = n1 / 10
		if digito == 2 or digito == 3 or digito == 5 or digito == 7:
			cont1 += 1

	while n2 > 0:
		digito1 = n2 % 10
		n2 = n2 / 10
		if digito1 == 2 or digito1 == 3 or digito1 == 5 or digito1 == 7:
			cont2 += 1

	if cont1 > cont2:
		print "El primer numero tiene la mayor cantidad de digitos primos, que son %d"%cont1 + " digitos."

	elif cont2 > cont1:
		print "El segundo numero tiene la mayor cantidad de digitos primos, que son %d"%cont2 + " digitos."

	else:
		print "Ambos numeros poseen la misma cantidad de digitos primos."
	
except ValueError:
	print "Error..."