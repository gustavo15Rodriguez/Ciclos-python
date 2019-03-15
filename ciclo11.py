#-*-coding:utf-8-*-

'''11. Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros
comprendidos entre un dígito y otro.'''

try:
	n = int(raw_input("Digite el primer numero de dos digitos:"))
	d1 = n/10
	d2 = n%10

	print "Los numeros comprendidos entre %d"%d1 + " y %d"%d2 + " son: "

	for i in range (d1, d2+1):
		print i

	for j in range (d2, d1+1):
		print j


except ValueError:
	print "Error..."
