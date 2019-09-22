from sys import stdin
"""
Ayuda de: https://www.geeksforgeeks.org/maximum-product-subarray/
"""
def pro(A):
	maximo=1
	minimo=1
	tmp=1
	for i in range (len(A)):
		if A[i]>0:	#POSITIVOS
			maximo=maximo*A[i]
			minimo=min(minimo,minimo*A[i])
		elif A[i]<0:	#NEGATIVOS
			tmp2=maximo			
			maximo=max(minimo*A[i],1) #minimo lleva el maximo valor negativo
									  #por eso al multiplicarlo por otro 
									  #negativo se convierte en el mayor positivo
			minimo=tmp2*A[i]
		else:	#CERO
			maximo=1
			minimo=1
		tmp=max(tmp,maximo)
	if tmp==1:	#Si tmp terminó en 1 es posible que 
				#el máximo valor esté en el array 
				#original
		tmp=max(A)
	return tmp

def main3():
	A=[]
	num=[1]
	while num!=[]:
		num = list(map(int, stdin.readline().split()))
		for n in num:			
			if n!=-999999:
				A.append(n)		
			else:
				print(pro(A))
				A=[]
main3()
