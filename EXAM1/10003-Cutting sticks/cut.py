INF=float("inf")
from sys import stdin
def solve2(inicio,fin):
	ans=INF
	if (inicio,fin) in MEMO:
		ans=MEMO[(inicio,fin)]
	else:
		for c in range(inicio+1,fin):
			if c in cortes:
				ans=min(ans,solve2(inicio, c)+solve2(c, fin)+fin-inicio)
	if ans!=INF:
		MEMO[(inicio,fin)]=ans
	else:
		ans=0
	return ans

def main():
	global cortes, MEMO
	tmp=True
	while tmp:
		read=int(stdin.readline())
		if read==0:
			tmp=False
		else:
			inicio=0;fin=read;MEMO=dict()
			stdin.readline()
			cortes=(stdin.readline().split())
			for i in range(len(cortes)):
				cortes[i]=int(cortes[i])
			print("The minimum cutting is",str(solve2(inicio,fin))+".")
main()