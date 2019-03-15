#-*-coding:utf-8-*-

'''37. Generar todas las tablas de multiplicar del 1 al 10.'''

try:
	mult= 0
	
	for i in range (1,11):
		print"\n"
		print "La tabla de multiplicar del numero: %d"%i
		for j in range(1,11):
			mult = i * j
			print "%d"%i +"*"+"%d"%j +"= %d"%mult

	
except ValueError:
	print "Error..."
