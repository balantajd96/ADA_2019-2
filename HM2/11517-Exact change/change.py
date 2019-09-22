from sys import stdin
import bisect
import math 
import copy
INF = math.inf

def solve2(l,M,C):
	global INF
	"""
	l: lista base
	M: lista de monedas
	C: costo de la compra
	"""
	ciclo=0
	tmp=[0]
	for m in M:        #Moneda
		j=len(tmp)-1
		tmp2=[]
		while j>=0:
			if m>C:
				l[m]=1
				j=-1
			else:
				if tmp[j]<C:
					l[tmp[j]+m]=min(l[tmp[j]+m], 1+l[tmp[j]])
					tmp2.append(tmp[j]+m)
				j-=1

		for t in tmp2:    #actualizo la lista de índices
			if not(t in tmp):
				bisect.insort(tmp, t)
	k=C
	while(l[k]==INF):
		k+=1
	return k,l[k]

def main():
	M=[];
	tcnt=int(stdin.readline())
	l=[INF for _ in range(20001)]
	l[0]=0
	l_copy=copy.copy(l)
	while tcnt!=0:
		C = int(stdin.readline())
		nums = int(stdin.readline())
		for i in range(0,nums):
			M.append(int(stdin.readline()))
		print(solve2(l,M,C));M=[];l=copy.copy(l_copy)
		tcnt -= 1
main()