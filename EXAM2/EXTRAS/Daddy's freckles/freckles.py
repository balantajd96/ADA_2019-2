import math


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


def kruskal(G, lenv):
  global df
  """
  G:    Graph
  lenv: number of vertices (intersections)
  """
  ans = list()
  G.sort(key=lambda x: x[2])
  df = dforest(lenv)
  for u,v,w in G:
    if df.find(u)!=df.find(v):
      ans.append((u, v, w))
      df.union(u, v)
  return ans


def solve(coord, lenv):
  """
  G:    Graph
  lenv: number of vertices (intersections)
  """
  G=[]
  for i in range(lenv):
    for j in range(i+1, lenv):
        dist=math.sqrt( ((coord[i][0]-coord[j][0])**2) + ((coord[j][1]-coord[i][1])**2) )
        G.append((i,j,dist))
  print(G)
  tmp=kruskal(G,lenv)
  ans=0
  for i in range(len(tmp)):
    ans+=tmp[i][2]
  return ans


def main():
  G=[(0,1,3),(0,2,5),(1,2,10),(2,0,5)]
  lenv=len(G)
  ans=(solve(G,lenv))
  print("Minimum ink used: {}".format(ans))
main()