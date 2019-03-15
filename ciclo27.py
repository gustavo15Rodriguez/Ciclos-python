#-*-coding:utf-8-*-

'''27.Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos. '''

try:
	n1 = int(raw_input("Digite el primer numero: "))
	n2 = int(raw_input("Digite el segundo numero: "))

	cont1 = 0
	cont2= 0

	while n1 > 0:
		digito = n1 % 10
		cont1 +=1
		n1 = n1 / 10

	while  n2 > 0:
		digito1 = n2 % 10
		cont2 +=1
		n2 = n2 / 10

	if cont1 > cont2:
		print "El primer numero ingresado posee la mayor cantidad de digitos que son: %d"%cont1

	elif cont2 > cont1:
		print "El segundo numero ingresado posee la mayor cantidad de digitos que son: %d"%cont2

	else:
		print "Ambos numeros poseen la misma cantidad de digitos."

except ValueError:
	print "Error..."