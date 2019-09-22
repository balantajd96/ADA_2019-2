from sys import stdin
def solve(A,lena):
	lis,lds=[ None for _ in range(lena)], [None for _ in range(lena)]
	tmp=-1
	for n in range(lena):
		lis[n]=lds[n]=1
		for i in range(n):
			if A[i]<=A[n] and lis[i]>=lis[n]: lis[n]=lis[i]+1
			if A[i]>=A[n] and lds[i]>=lds[n]: lds[n]=lds[i]+1
		t=lis[n]+lds[n]-1
		if t>tmp:tmp=t
	return tmp

def main():
	#main de Toro
	tcnt = int(stdin.readline())
	while tcnt != 0:
		tcnt2 = int(stdin.readline())
		arr = []
		lena = tcnt2
		while tcnt2 != 0:
			num = list(map(int, stdin.readline().split()))
			arr=arr+num
			tcnt2 -= 1
		if lena == 0:return 0
		else: 
			arr.reverse()
			print(solve(arr, lena))
		tcnt -= 1

main()