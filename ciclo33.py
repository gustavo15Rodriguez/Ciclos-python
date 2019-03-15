#-*-coding:utf-8-*-r

'''33. Si 32768 es el tope superior para los números entero cortos, determinar cuál es el
número primo más cercano por debajo de él.'''

try:
	cont = 0

	for i in range (32767,32740,-1):
		cont = 0
		for j in range (1,i+1):
			if i %j == 0:
				cont +=1

		if cont == 2:
			print "El numero primo mas cercano a 32768 es: %d"%i
			break

except ValueError:
	print "Error..."