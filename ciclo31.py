#-*-coding:utf-8-*-

'''31. Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los
números terminados en 5.'''

try:
	numero = 1
	cont = 0
	suma = 0
	prom = 0

	while numero != 0:
		numero = int(raw_input("Digite el numero deseado: "))
		if numero%10 == 5:
			suma+=numero
			cont +=1
			prom = suma/cont
			
	if numero%10 == 0:
		print "El promedio de los numeros terminados en 5 es igual a: %d"%prom

except ValueError:
	print "Error..."	
