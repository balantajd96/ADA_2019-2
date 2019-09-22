def BinarySearch(A, lo, hi, x):
	"""
	A: Array
	hi: left limit
	lo: right limit
	x: element
	"""
	ans=-1
	if lo+1==hi:
		if A[lo]==x:
			ans=lo
	else:
		mid=(hi+lo)>>1
		if A[mid]>x:
			ans=BinarySearch(A, lo, mid, x)
		elif A[mid]<x:
			ans=BinarySearch(A, mid, hi, x)
		else:
			ans=mid
	return ans

def BinarySearch2(A, lo, hi, x):
	"""
	A: Array
	hi: left limit
	lo: right limit
	x: element
	"""
	ans=-1
	if lo+1==hi:
		if A[lo]>x:
			ans=A[lo]
		if A[lo+1]>x:
			ans=A[lo+1]
	else:
		mid=(hi+lo)>>1
		if A[mid]<x:
			ans=BinarySearch2(A, mid, hi, x)
		elif A[mid]>x:
			ans=BinarySearch2(A, lo, mid, x)
		else:
			ans=A[mid+1]
	return ans

def BinarySearchI(A, lo, hi, x):
	"""
	Búsqueda binaria que encuentra el primer número
	mayor a x
	"""
	ans=-1
	if lo==hi:
		if A[lo]>x:
			ans=A[lo]
	elif len(A)!=0:
		while lo+1<hi:
			mid=(lo+hi)>>1
			if A[mid]<=x:
				lo=mid+1
			else:
				hi=mid
		if A[lo]>x:
			ans=A[lo]
		elif A[hi]>x:
			ans=A[hi]
	return ans



def main():
	A=[2,7,8,9,23,25,101,120,121]
	for i in range(125):
		print(i, BinarySearch2(A,0,len(A)-1,i))	
	
#main()
A=[2,7,8,9,23,25,101,120,121]
A2=[2,7,8,9,23,25,101,120,121,200]
print(BinarySearchI(A,0,len(A)-1, 122))