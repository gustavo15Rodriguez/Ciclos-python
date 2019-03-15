#-*-coding:utf-8-*-

'''9. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.'''

try:
	for i in range (25, 205+1):
		if i%10==6:
			print i

except ValueError:
	print "Error..."
