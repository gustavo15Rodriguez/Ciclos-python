#-*-coding:utf-8-*-

'''49. Utilizando ciclos anidados generar las siguientes ternas de números
 
1   1   1
2   1   2
3   1   3
4   2   1
5   2   2
6   2   3
7   3   1
8   3   2
9   3   3 
'''

try:
	s = 0
	for i in range (1,4):
		for j in range (1,4):
			s+=1
			print s, i, j

except ValueError:
	print "Error..."
