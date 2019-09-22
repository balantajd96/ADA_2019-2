from sys import stdin
def solve(arr):
	"""
	Ayuda de Alirio y David H.
	"""
	ans=0
	N=str(bin(arr[0]))[2:]
	tmp=''
	for i in range(32-len(N)):tmp=tmp+'0'
	N=tmp+N
	L=arr[1];U=arr[2]
	j=31
	for i in range(32): #Revisar len(n)
		tmp=1<<j
		if ans+tmp<=U and N[i]=='0':
			ans+=tmp
		elif ans+tmp<=L and N[i]=='1':
			ans+=tmp
		j-=1
	return ans
	
def main():
	tmp=True
	while tmp:
		N=stdin.readline().split()
		if N==[]:
			tmp=False
		else:
			arr1=[int(x) for x in N]
			print(solve(arr1))
main()