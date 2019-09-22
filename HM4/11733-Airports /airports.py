from sys import stdin
class dforest(object):
  """Disjoint-Union implementation with disjoint forests using path
  compression and ranking"""

  def __init__(self, size=100):
    """create an empty disjoint forest"""
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 0 for _ in range(size) ]

  def __str__(self):
    """return the string representation"""
    return str(self.__parent)
  
  def find(self, x):
    """return the representative of x"""
    if self.__parent[x]!=x: self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]

  def union(self, x, y):
    """perform the union of the collections where x and y belong"""
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      krx,kry = self.__rank[rx],self.__rank[ry]
      if krx>=kry:
        self.__parent[ry] = rx
        if krx==kry: self.__rank[rx] += 1
      else:
        self.__parent[rx] = ry

def kruskal(G, lenv, A):
  global df
  """
  G:    Grafo
  lenv: cantidad de vértices
  A: max cost of building a road
  """
  ans = list()
  G.sort(key=lambda x: x[2])
  df = dforest(lenv)
  for u,v,w in G:
    if df.find(u)!=df.find(v) and w<A:
      #it may be cheaper to build an airport than a road
      ans.append((u, v, w))
      df.union(u, v)
  return ans

def solve(arr,A,N):
  """
  arr: array with locations
  A: cost of building an airport
  """
  global df
  road_cost=0; airports=0
  for i in range(len(arr)): road_cost+=arr[i][2]
  for i in range(N):
    if df.find(i)==i: airports+=1
  return road_cost+(A*airports), airports

def main():
  """
  Ayuda de Jhoan L. y Nicolás O.
  Implementación de Kruskal tomada de la página del curso 2019-1
  Esta implementación de Kruskal fue explicada en clase por
  Miguel
  
  N: number of locations
  M: number of possible roads that can be built
  A: cost of building an airport
  X,Y: are two locations
  C:cost of building a road between X and Y
  """
  cnt=int(stdin.readline())
  tmp=1
  while cnt!=0:
    N,M,A = map(int,stdin.readline().split())
    G=[]
    for i in range(M):
      X,Y,C = map(int,stdin.readline().split())
      G.append((X-1,Y-1,C))
    arr=kruskal(G,N,A)
    cost,airports=solve(arr,A,N)
    print("Case #{0}: {1} {2}".format(tmp,cost,airports))
    cnt-=1;tmp+=1
main()