#-*-coding:utf-8-*-

'''25.	Leer un número entero y determinar a cuánto es igual el promedio entero de sus dígitos.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	
	suma = 0
	cont = 0
	prom = 0

	while numero > 0:
		digito = numero % 10
		suma = suma + digito
		cont +=1
		numero = numero / 10
		prom = suma / cont 
	print suma
	print "El promedio entero de los digitos del numero ingresado es igual a: %d"%prom
	
except ValueError:
	print "Error..."