from sys import stdin
MAX=-9999999


def solve(index, ans):
	global arr, train, n, MAX, lines
	if ans>MAX:MAX=ans
	if index<lines:
		for j in range(index, lines):
			ok=True
			tmp=list(train)

			i=arr[j][0]
			while i<arr[j][1] and ok: #Fill the train while possible
				if train[i]+arr[j][2]>n:
					ok=False
				train[i]+=arr[j][2]
				i+=1
			if ok: #if there is no overcrowding
				c=(arr[j][1]-arr[j][0])*arr[j][2]
				solve(j+1, ans+c)
			train=tmp #the order is canceled


def main():
	global arr, MAX, n, train, lines
	tmp=True
	while tmp:
		n,B,lines=map(int, stdin.readline().split())
		if not (n==0 and B==0 and lines==0):
			arr=[]; train=[]; MAX=-9999999
			for _ in range(B+1):
				train.append(0)

			for _ in range(lines):
				src,dest,cnt=map(int, stdin.readline().split())
				arr.append((src, dest, cnt))
			arr.sort(key=lambda x: x[0])
			solve(0, 0)
			print(MAX)
		else:
			tmp=False           
main()