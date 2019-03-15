#-*-coding:utf-8-*-

'''8. Mostrar en pantalla todos los pares comprendidos entre 20 y 200.'''

try:
	for i in range (20, 200+1):
		if i%2==0:
			print i

except ValueError:
	print "Error..."
