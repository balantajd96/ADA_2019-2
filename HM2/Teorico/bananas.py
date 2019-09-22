def bananas(A,B,C):
	"""
	Este algoritmo tiene como objetivo 
	verificar si dos cadenas dadas están
	mezcladas en una tercera cadena.

	Entrada:
		A -> arreglo con la palabra A
		B -> arreglo con la palabra B
		C -> arreglo con la posible
			 mezcla de A y B
	Salida: True si A y B están en C
			False de otro modo
	"""
	a=0; b=0
	ans=True
	if len(A)+len(B)!=len(C):
		ans=False
	else:
		while ans and (a<len(A) and b<len(B)):
			if A[a]==C[a]:
				a+=1
			elif B[b]==C[b]:
				b+=1
			else:
				ans=False
	return ans
#Complejidad temporal: 

def ref1(A,B,C):
	a,b,cnt_a,cnt_b,cnt=0,0,0,0,0
	ans=True

	while ans and (a<len(A) or b<len(B)):
		print(a,b, cnt)
		if cnt_a+2==cnt_b:
			if a>=len(A):
				ans=False
			else:
				if A[a]==C[cnt]:
					a+=1; cnt_a+=1; cnt_b=0; cnt+=1
				else:
					ans=False
		elif cnt_b+2==cnt_a:
			if b>=len(B):
				ans=False
			else:
				if B[b]==C[cnt]:
					b+=1; cnt_a=0; cnt_b+=1; cnt+=1
				else:
					ans=False
		else:
			b=1
			if a>=len(A):
				if B[b]==C[cnt]:
					b+=1; cnt_a=0; cnt_b+=1; cnt+=1
					b=0
			if b>=len(B):
				if A[a]==C[cnt]:
					a+=1; cnt_a+=1; cnt_b=0; cnt+=1
					b=0
			if b:
				ans=False

	return ans,a,b,cnt_a,cnt_b



a="DYNAMIC"
b="PROGRAMMING"
c="PRDOYGNARAMMMIICNG"
A=list(a); B=list(b)
C=list(c)
print(ref1(A,B,C))



