#-*-coding:utf-8-*-

'''18. Leer dos números entero y mostrar todos los múltiplos de 5 comprendidos entre el
menor y el mayor.'''

try:
	n1 = int(raw_input("Digite el primer numero: "))
	n2 = int(raw_input("Digite el segundo numero: "))

	for i in range(n1, n2+1):
		if i%5==0:
			print i

	for i in range(n2, n1+1):
		if i%5==0:
			print i
	

except ValueError:
	print "Error..."	