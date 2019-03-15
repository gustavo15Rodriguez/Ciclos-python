#-*-coding:utf-8-*-

'''14. Mostrar en pantalla los primeros 20 múltiplos de 3.'''

try:
	cont = 0
	print "Los primeros 20 multiplos de 3 son: "

	for i in range (1, 100):
		if i%3== 0:
			print i
			cont+=1

		if cont == 20:
			break


except ValueError:
	print "Error..."
