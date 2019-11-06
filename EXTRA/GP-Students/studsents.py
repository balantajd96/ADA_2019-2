import random
def solution(A):
	rows=[]; maxi=[]
	for a in A:
		if len(rows)==0:
			rows.append([a])
			maxi.append(a)
		else:
			i=0
			while i<len(maxi):
				if a<=maxi[i]:
					rows[i].append(a)
					i=len(maxi)+1
				i+=1
			if i==len(maxi):
				rows.append([a])
				maxi.append(a)
	return len(rows)

def main():
	A=[]
	tmp2=""
	for _ in range(1000):
		tmp=random.randint(1, 10000)
		tmp2=tmp2+str(tmp)+","
		A.append(tmp)
	print(tmp2)
	print(solution(A))


main()
