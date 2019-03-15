#-*-coding:utf-8-*-

'''30. Leer un número entero y mostrar todos sus componentes numéricos o sea aquellos para
quienes él sea un múltiplo.'''

try:
	numero = int(raw_input("Digite el primer numero: "))

	print "Los componentes numericos del numero %d son:"%numero
	
	for i in range (1,numero+1):
		if numero % i == 0:
			print i
	
except ValueError:
	print "Error..."