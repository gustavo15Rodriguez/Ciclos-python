#-*-coding:utf-8-*-

'''15. Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.'''

try:
	cont = 0
	suma = 0

	for i in range (1, 100):
		if i%3== 0:
			cont+=1
			suma = suma + i

		if cont == 20:
			break

	print "La suma de los primeros 20 multiplos de 3 es: %d"%suma

except ValueError:
	print "Error..."
