from sys import stdin
def sort(N,arr1, arr2):
	tmp1=[]; tmp2=[]
	for i in range(N):
		if arr1[i]<arr2[i]:
			tmp1.append((arr1[i],arr2[i]))
		else:
			tmp2.append((arr1[i],arr2[i]))
	tmp1.sort(key=lambda item: (item[0]),reverse=False)
	tmp2.sort(key=lambda item: (item[1]),reverse=True)
	l=tmp1+tmp2
	return l

def solve(N,arr1, arr2):
	datos=sort(N,arr1,arr2)
	suma_s=0; suma_g=0
	for i in range(N):
		suma_s+=datos[i][0]
		suma_g=max(suma_s,suma_g)+datos[i][1]
	return suma_g
	
def main():
	tmp=True
	while tmp:
		N=stdin.readline()
		if N=="":
			tmp=False
		else:
			arr1=[int(x) for x in stdin.readline().split()]
			arr2=[int(x) for x in stdin.readline().split()]
			print(solve(int(N),arr1,arr2))
main()
