#-*-coding:utf-8-*-

'''50. Utilizando ciclos anidados generar las siguientes parejas de números
 
0   1
1   1
2   1
3   1
4   2
5   2
6   2
7   2 
'''

try:
	s = 0
	for i in range (1,3):
		for j in range (4):
			print s, i
			s +=1

except ValueError:
	print "Error..."
