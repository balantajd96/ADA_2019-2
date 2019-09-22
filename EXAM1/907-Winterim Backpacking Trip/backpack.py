import time
from sys import stdin
def valido(mid,k,costos):
	ans=True
	tmp=mid;i=0
	while i<len(costos) and ans:
		if tmp>=costos[i]: #Pueden seguir caminando
			tmp-=costos[i]
		else:			   #Les toca dormir
			k-=1
			tmp=mid-costos[i]
		if k<0 or tmp<0:   #Ya acamparon los k días o 
						   #no alcanzan a acabar el viaje
			ans=False
		
		i+=1
	return ans

def solve2(N,k,arreglo):
	ans=float("inf");SUMA=0
	for i in range(0,len(arreglo)):SUMA+=arreglo[i]
	lo=0;hi=SUMA
	if k==0:
		ans=SUMA
	else:
		while lo<=hi:
			mid=(lo+hi)>>1
			if valido(mid,k,arreglo):
				ans=min(ans,mid)
				hi=mid-1
			else:
				lo=mid+1
	return ans

def main():
	global N,K,num
	tmp=True
	while tmp:
		read=stdin.readline().split()
		if read==[]:
			tmp=False
		else:
			N=int(read[0])
			k=int(read[1])
			arreglo=[]
			for i in range(N+1):
				arreglo.append(int(stdin.readline()))
			print(solve2(N,k,arreglo))
#print(solve(6,2,[53,23,45,7,70,80,37]))
begin=time.time()
main()
end=time.time()
#print(end-begin)