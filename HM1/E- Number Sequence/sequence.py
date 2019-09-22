from sys import stdin
def lista_sumas():
	#(n+1)k-11(1 k-veces)
	#	n: es el número al cual quiero llegar
	#	k: número de cifras del número
	#https://www.youtube.com/watch?v=EMQ79oJ-f4M
	l=[];suma=0
	uno=[1,11,111,1111,11111,111111,111111,1111111,11111111]
	for n in range(1,31271):
		k=len(str(n))
		unos=uno[k-1]
		suma+=((n+1)*k)-unos
		l.append(suma)
	return l

def suma(n):
	l=[];suma=0
	uno=[1,11,111,1111,11111,111111,111111,1111111,11111111,111111111,1111111111]
	k=len(str(n))
	unos=uno[k-1]
	suma=((n+1)*k)-unos
	l.append(suma)
	return suma
def BinarySearchI(A,lo,hi,x,length):
	"""
	Búsqueda binaria que encuentra el primer número
	menor a x
	"""
	ans=-1
	if lo==hi:
		if A[lo]>x:
			ans=A[lo]
	elif length!=0:
		while lo+1<hi:
			mid=(lo+hi)>>1
			if A[mid]<=x:
				lo=mid+1
			else:
				hi=mid
		if A[lo]>x:
			ans=A[lo-1]
			if ans==x: ans=A[lo-2]
		elif A[hi]>x:
			ans=A[hi-1]
			if ans==x: ans=A[hi-2]
	return ans
def solve(l,x,digitos):
	ans=-1;
	lo=0;hi=31270
	tmp=BinarySearchI(l,lo,hi,x,hi-lo)
	if tmp==x:
		ans=digitos[x-1]
	else:
		ans=digitos[x-tmp-1]
	return ans
def main():
	tcnt = int(stdin.readline())
	while tcnt!=0:
		print(solve(LISTA,int(stdin.readline()),DIGITOS))
		tcnt -= 1


LISTA=lista_sumas()
DIGITOS="".join(str(i) for i in range(1,31270))
main()
