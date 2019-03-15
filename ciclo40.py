#-*-coding:utf-8-*-

'''40. Leer un número de dos dígitos y determinar si pertenece a la serie de Fibonacci.'''

try:
	n1 = int(raw_input("Digite un numero de dos digitos: "))

	contador = 0

	if n1 >9 and n1 <=99:
		inicial = 0
		numero = 1
		ultimo = 0
		penultimo = 0

		

		for i in range(0,20):
			penultimo = ultimo
			ultimo = numero
			numero = penultimo + ultimo

			if n1 == numero:
				print "El numero ingresado pertenece a la serie Fibonacci."
				contador+=1

	else:
		print "El numero ingresado debe ser de dos digitos."


	if contador != 1 and n1 >9 and n1<= 99:
		print "El numero ingresado no pertenece a la serie Fibonacci."

except ValueError:
	print "Error..."
