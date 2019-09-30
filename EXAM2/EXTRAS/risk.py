from heapq import heappop,heappush
from sys import stdin
INF = float('inf')

def sssp(G,source, objective):
	"""G is a graph representation in adjacency list format with vertices
		 in the set { 0, ..., |V|-1 } and source a vertex in G"""
	# dist[u] : "minimum distance detected from source to u
	dist = [ INF for i in range(len(G)) ] ; dist[source] = 0
	visited = [ False for i in range(len(G)) ]
	heap = [ (0,source) ]
	while len(heap)!=0:
		d,u = heappop(heap)
		if not(visited[u]):
			visited[u] = True
			for v,w in G[u]:
				if dist[v]>d+w:
					dist[v] = d+w
					heappush(heap,(dist[v],v))
	return dist[objective]

def solve(src, obj, P, C):
	"""
	P: list of neighbors of ith country
	C: list of cost of attacking ith country
	"""
	G=[ [] for i in range(len(P)) ]
	for i in range(len(P)):
		for j in range(len(P[i])):
			tmp=(P[i][j],C[P[i][j]])
			G[i].append(tmp)

	return=sssp(G, src, obj)
	
def main():
	src=0
	obj=7
	P=[[1],
		 [0,2,3,4],
		 [1,2,5],
		 [1,2,4,5],
		 [1,3,5],
		 [2,3,4,6,7],
		 [5,7],
		 [5,6]]
	C=[2,2,5,2,1,5,3,10]
	solve(src,obj,P,C)
main()