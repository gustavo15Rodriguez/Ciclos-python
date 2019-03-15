#-*-coding:utf-8-*-

'''16. Mostrar en pantalla el promedio entero de los n primeros múltiplos de 3 para un 
número n leído.'''

try:
	n = int(raw_input("Digite el numero deseado: "))

	mult = n * 3
	cont = 0
	suma = 0
	prom = 0

	for i in range (1, mult+1):
		if i%3 == 0:
			suma+= i
			cont += 1

	prom = 	suma // cont
	print "El promedio de los primeros %d"%n + " numeros es: %d"%prom	

	
except ValueError:
	print "Error..."
