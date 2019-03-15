#-*-coding:utf-8-*-

'''19. Leer un número entero y determinar si es primo.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))
	cont = 0

	for i in range (1, numero+1):
		if numero % i == 0:
			cont += 1

	if numero == 1:
		print "El numero %d"%numero + " no es primo."

	elif cont != 2:
		print "El numero %d"%numero + " no es primo."

	else:
		print "El numero %d"%numero + " es un numero primo."

except ValueError:
	print "Error..."	