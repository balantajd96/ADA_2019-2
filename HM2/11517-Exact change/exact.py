from sys import stdin
import math
INF = math.inf
datos=dict()
def v(D,C,n):
	"""
	Ayuda de Verónica y Tania
	D: arreglo con las monedas
	C: costo de la compra
	n: indice
	"""
	global datos
	if ((C,n) in datos):
		ans=datos[(C,n)]
	else:
		if C<=0 and n==0:
			ans=(0,0)
		elif C!=0 and n==0:
			ans=(INF,INF)
		else:
			tupla1 = v(D,C-D[n-1],n-1)
			ans=((D[n-1]+tupla1[0],1+tupla1[1]))
			tupla2=v(D,C,n-1)
			if ans[0]<tupla2[0]:
				ans=ans
			elif ans[0]>tupla2[0]:
				ans=tupla2
			else:
				if ans[1]<tupla2[1]:
					ans=ans
				else:
					ans=tupla2		
		datos[(C,n)]=ans
	return ans


def main():
	global l, datos
	D=[];
	tcnt=int(stdin.readline())
	while tcnt!=0:
		datos=dict()
		datos[0]=0
		C=int(stdin.readline())
		nums=int(stdin.readline())
		for i in range(0,nums):
			D.append(int(stdin.readline()))
		tmp=(v(D,C,len(D)))
		print(tmp[0],tmp[1])
		D=[]
		tcnt -= 1
main()