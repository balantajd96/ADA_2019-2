from heapq import heappop,heappush
from sys import stdin
INF = float('inf')

def sssp(G,source):
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
  return dist

def solve(G,E,T,N):
  ans=0
  for i in range(N+1):
    distances=sssp(G,i)
    if distances[E]<=T:
      ans+=1
  return ans
def main():
  """
  Implementación de Dijkstra tomada de la página del curso 2019-1
  Esta implementación fue explicada en clase por Miguel
  """
  """
  G = [ [(1,2),(2,5),(3,2)],
        [(2,5),(2,10),(3,2)],
        [(1,7),(3,8),(3,1)],
        [(1,5),(2,10),(2,2)] ]

  cost=sssp(G,0)
  """
  cnt=int(stdin.readline())
  while cnt!=0:
    stdin.readline()
    tmp=[]
    for i in range(4):
      tmp.append(int(stdin.readline()))
    N=tmp[0];E=tmp[1];T=tmp[2];M=tmp[3]
    G=[ [] for i in range(N+1) ]
    for i in range(M):
      a,b,w = map(int,stdin.readline().split())
      G[a].append((b,w))
    #print(G)
    if cnt!=1:print("{0}\n".format(solve(G,E,T,N)))
    else:print("{0}".format(solve(G,E,T,N)))
    cnt-=1
main()