from sys import stdin

INF = float('inf')
memo = None

def tsp_dp(v, A, vs, adj, n):
  global memo
  ans = INF
  if (v,A) in memo:
    ans = memo[(v,A)]
  else:
    if A == ((1<<n) - 1):
      ans = adj[v][vs]
    else:
      for i in range(n):
        if i != v and (A & (1<<i)) == 0:
          ans = min(ans, adj[v][i] + tsp_dp(i, (A | (1<<i)), vs, adj, n))
    memo[(v,A)] = ans
  return ans


def solve(beepers,n):
	""" create the adjacency matrix"""
	adj=[]
	for i in range(n):
		tmp=[]
		for j in range(n):
			dist=abs(beepers[i][0]-beepers[j][0])+abs(beepers[i][1]-beepers[j][1])
			tmp.append(dist)
		adj.append(tmp)
	return tsp_dp(0,0,0,adj,n)
	

def main():
	global memo
	"""	Input and output """
	T=int(stdin.readline())
	while T>0:
		stdin.readline()
		x, y=map(int, stdin.readline().split())
		n=int(stdin.readline())
		beepers=[]
		beepers.append((x,y))
		memo=dict()
		for _ in range(n):
			a, b=map(int, stdin.readline().split())
			beepers.append((a,b))
		beepers.append((x,y))
		n+=1
		print("The shortest path has length",solve(beepers,n))
		T-=1
main()
