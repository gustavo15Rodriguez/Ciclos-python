#-*-coding:utf-8-*-

'''4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.'''

try:
	n1 = int(raw_input("Digite el primer numero: "))
	n2 = int(raw_input("Digite el segundo numero: "))

	for i in range (n1, n2+1):
		if n1<n2:
			print i


	for j in range (n2, n1+1):
		if n2<n1:
			print j

except ValueError:
	print "Error..."
