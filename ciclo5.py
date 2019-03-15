#-*-coding:utf-8-*-

'''5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.'''

try:
	n1 = int(raw_input("Digite el primer numero: "))
	n2 = int(raw_input("Digite el segundo numero: "))

	for i in range (n1, n2+1):
		if i%10 == 4:
			print i


	for j in range (n2, n1+1):
		if j%10 == 4:
			print j
		

except ValueError:
	print "Error..."
