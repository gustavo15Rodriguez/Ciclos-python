#-*-coding:utf-8-*-

'''17. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y
primeros múltiplos de 5 para valores de x y y leídos.'''

try:
	n1 = int(raw_input("Digite el primer valor: "))
	n2 = int(raw_input("Digite el segundo valor: "))

	mult = n1 * 2
	mult1 = n2 * 5
	cont = 0
	cont1 = 0
	suma = 0
	suma1 = 0
	prom = 0
	prom1 = 0

	for i in range (1, mult+1):
		if i%2== 0:
			suma += i
			cont +=1
	prom = suma // cont	
	print "El promedio 1 es: %d"%prom	

	for j in range (1, mult1+1):
		if j%5== 0:
			suma1 += j
			cont1 +=1
	prom1 = suma1 // cont1
	print "El promedio 2 es: %d"%prom1	


	if prom>prom1:
		print "El promedio 1: %d"%prom + " es mayor al promedio 2 que es: %d"%prom1

	if prom1>prom:
		print "El promedio 2: %d"%prom1 + " es mayor al promedio 1 que es: %d"%prom


except ValueError:
	print "Error..."	