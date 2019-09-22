import math
from sys import stdin
INF=float("inf")
def solve(a,e,h):
	"""
	a:	indice de una asignatura
	e:	horas de estudio
	h:	horas disponibles
	NOTAS:	tabla con las notas según horas y asignaturas
	E:	Maximo de horas de estudio
	"""	
	ans=-INF
	print(a,e,h)


	if a==0:
		print("---->",1)
		ans=0
	elif a!=0 and e==0:
		print("---->",2)
		ans=-INF			
	elif a!=0 and e!=0 and NOTAS[a-1][e-1]<5:
		print("---->",3)
		ans=solve(a,e-1,h)
		#ans=-INF		
	elif a!=0 and e!=0 and NOTAS[a-1][e-1]>=5 and h<e:
		print("---->",4)
		ans==solve(a,e-1,h)			
	elif a!=0 and e!=0 and NOTAS[a-1][e-1]>=5 and h>=e:
		print("---->",5)
		ans=max(solve(a,e-1,h),
				solve(a-1,E,h-e)+NOTAS[a-1][e-1])
			

	return ans


def main():
  global DATOS, E, NOTAS; INF=float("inf")
  tcnt = int(stdin.readline())
  while tcnt!=0:
  	tmp=list(map(int, stdin.readline().split()))
  	A=int(tmp[0]); E=int(tmp[1])
  	NOTAS=[]
  	DATOS=dict()
  	#NOTAS = [ [ -INF for c in range(E) ] for n in range(A+1) ]
  	for i in range(A):
  		NOTAS.append(list(map(int, stdin.readline().split())))
  		print(NOTAS[i])
  	print(solve(A,E,E))
  	for i in DATOS:
  		print(i, DATOS[i])
  	tcnt-=1
main()