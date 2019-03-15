#-*-coding:utf-8-*-

'''3. Leer un número entero y mostrar todos los divisores exactos del número comprendidos
entre 1 y el número leído.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	for i in range (1, numero):
		if numero % i == 0:
			print "Los divisores comprendidos entre 1 y %d"%numero + " son: %d"%i 



except ValueError:
	print "Error..."
