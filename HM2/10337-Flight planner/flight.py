import math
from sys import stdin
INF=float("inf")
def phi(a,m):
	"""
	Función realizada de manera conjunta con:
		Verónica T
		Laura A
		Danilo M
		Juan C Vanegas
	"""
	ans=0
	if tab[a][m]!=INF:
		ans=tab[a][m]
	else:
		if a==9 and m==0:
			ans=0
		elif (m==0 and a!=9):	
			ans=INF
		else:	
			if m!=0 and (0<a<9):
				ans=min(phi(a-1,m-1)+60-W[a-1][m-1],
						phi(a+1,m-1)+20-W[a+1][m-1],
						phi(a,m-1)+30-W[a][m-1])
			elif m!=0 and a==9:
				ans=min(phi(a-1,m-1)+60-W[a-1][m-1],
						phi(a,m-1)+30-W[a][m-1])
			elif m!=0 and a==0:
				ans=min(phi(a+1,m-1)+20-W[a+1][m-1],
						phi(a,m-1)+30-W[a][m-1])
		tab[a][m]=ans

	return ans

def main():
  global W, tab; INF=float("inf")
  tcnt = int(stdin.readline())
  while tcnt!=0:
  	nada=stdin.readline()
  	m=int(stdin.readline())//100
  	W=[]
  	tab = [ [ INF for c in range(m+1) ] for n in range(11) ]
  	tab[0][0]=0
  	for i in range(10):
  		W.append(list(map(int, stdin.readline().split())))
  	print(phi(9,m))
  	print()
  	tcnt-=1
main()