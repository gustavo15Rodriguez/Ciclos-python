#-*-coding:utf-8-*-

'''13. Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número
leído.'''

try:
	n = int(raw_input("Digite el numero deseado: "))

	print "Los multiplos de 5 comprendidos entre 1 y %d"%n + " son: "

	for i in range(1, n+1):
		if i%5== 0:
			print i



except ValueError:
	print "Error..."
