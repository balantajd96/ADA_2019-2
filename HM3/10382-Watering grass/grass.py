from sys import stdin
def sort_ran(arr):
	"""
	toma dos arreglos, los junta en tuplas
	y los ordena de mayor a menor por posicion.
	Después pasa a distancias por medio de 
	tuplas7
	"""
	new_arr=[]
	for i in range(len(arr)):
		hi=arr[i][0]+arr[i][1]-1
		lo=arr[i][0]-arr[i][1]+1
		new_arr.append((lo,hi))
	new_arr.sort(key=lambda item: (item[0],item[1]),reverse=False)
	return new_arr

def solve3(N,l,w,arr):
	m=max(l,w); cnt=1
	i=0; ranges=sort_ran(arr)

	if ranges[0][0]>0:
		cnt=-1
	else:
		for i in range(len(ranges)):
			if ranges[i][0]<0 and ranges[i][1]>=m:
				return 1
		lo=ranges[0][0]
		hi=ranges[0][1]
		i=1
		while i<N:
			candidates=[]
			limit=hi
			while i<N and limit-ranges[i][0]>=-1:
				candidates.append((ranges[i][0],ranges[i][1]))
				i+=1
			maxi=-9999; chosen=None
			for j in range(len(candidates)):
				diff=candidates[j][1]
				if diff>maxi:
					maxi=diff
					chosen=j			
			hi=candidates[chosen][1]
			cnt+=1
		if hi<=m:cnt=-1
	return cnt

def main():
	tmp=True
	while tmp:
		try:
			N,l,w=map(int, stdin.readline().split())
			arr=[]
			for i in range(N):
				pos,r=map(int, stdin.readline().split())
				arr.append((pos,r))
			print(solve3(N,l,w,arr))
		except:
			tmp=False			
main()