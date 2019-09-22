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
	ans=0
	if (a,e,h) in DATOS:
		ans=DATOS[(a,e,h)]
	else:
		if a==A:
			ans=0
		elif a<A and h==0:
			ans=-INF
		elif a<A and h>0 and e>h:
			ans=-INF
		elif a<A and h>0 and e<=h and NOTAS[a][e]<5:
			ans=solve(a,e+1,h)
		elif a<A and h>0 and e<=h and NOTAS[a][e]>=5:
			ans=max(solve(a,e+1,h),
					solve(a+1,1,h-e) + NOTAS[a][e])
	DATOS[(a,e,h)]=ans
	return ans

def main():
  global DATOS, E, A,NOTAS; INF=float("inf")
  tcnt = int(stdin.readline())
  while tcnt!=0:
  	tmp=list(map(int, stdin.readline().split()))
  	A=int(tmp[0]); E=int(tmp[1])
  	NOTAS=[]
  	DATOS=dict()
  	for i in range(A):
  		tmp=[0]
  		NOTAS.append(tmp+list(map(int, stdin.readline().split())))
  	nota=round(solve(0,1,E)/A,2)
  	nota2="{0:.2f}".format(nota)
  	if nota>=5:
  		print("Maximal possible average mark -",nota2,end=".\n")
  	else:
  		print("Peter, you shouldn't have played billiard that much.")
  	tcnt-=1
main()
