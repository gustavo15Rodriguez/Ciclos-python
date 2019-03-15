#-*-coding:utf-8-*-

'''35. Leer dos números enteros y determinar a cuánto es igual el producto mutuo del primer
dígito de cada uno. '''

try:
	n1 = int(raw_input("Digite el primer numero deseado: "))
	n2 = int(raw_input("Digite el segundo numero deseado: "))


	while n1 >0:
		digito = n1 % 10	
		n1 = n1 / 10

	while n2 >0:
		digito1 = n2 % 10
		n2 = n2 / 10
	
	mult = digito * digito1

	print "El producto mutuo de los primeros digitos de los numeros ingresados es: %d"%mult
	

except ValueError:
	print "Error..."