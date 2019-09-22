import math
INF=math.inf
def hackers(n,L,H):
	"""
	Este algoritmo tiene como objetivo calcular el
	máximo beneficio que puede obtener un grupo de
	trabajo en una cantidad de semanas dadas y unos
	tipos de trabajos pagados según la semana en 
	que se realicen.

	Entrada: 
		n -> número de semanas
		L -> arreglo con las ganancias estrés bajo
		H -> arreglo con las ganancias estrés alto
	Salida: máximo beneficio con un plan según las
			entrada
	"""
	global DATOS #arreglo para memorizar

	if DATOS[n]!=-INF:
		ans=DATOS[n]
	else:
		if n<0:
			ans=0
		else:
			ans=max(hackers(n-1,L,H)+L[n-1],
					hackers(n-1,L,H)+0,
					hackers(n-2,L,H)+H[n-1])
		DATOS[n]=ans
	return ans
#Complejidad temporal: O(n)
n=4
DATOS=[-INF for _ in range(n)]
L=[10,1,10,10]
H=[5,50,100,1]
print(hackers(n-1,L,H))