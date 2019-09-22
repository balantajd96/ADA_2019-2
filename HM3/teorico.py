def BinarySearch(A, lo, hi, x):
  """
  Búsqueda binaria que encuentra el primer número
  mayor a x
  """
  ans=-1
  if lo==hi:
    if A[lo][1]>x:
      ans=A[lo][1]
  elif len(A)!=0:
    while lo+1<hi:
      mid=(lo+hi)>>1
      if A[mid][1]<=x:
        lo=mid+1
      else:
        hi=mid
    if A[lo][1]>x:
      ans=lo
    elif A[hi][1]>x:
      ans=hi
  return ans

def solve(L,R,P):
  """
  Objetivo:
    Encontrar la cantidad de mínima de cortes que se pueden hacer 
    con todos los elemento de P respecto a los rangos de L y R
  Entrada:
    L: arreglo con los puntos de inicio de cada segmento
    R: arreglo con los puntos de fin de cada segmento
    P: arreglo con los puntos que se espera crucen los segmentos
       creados con L y R posición a posición
  Salida:
    ans: arreglo de tuplas donde el primer valor de las tuplas es
         un elemento de P y el segundo valor es la cantidad de 
         segmentos que el elemento de P cortó
  """
  ans=[]
  arr=zip(L,R);arr.sort(key=lambda item: (item[1]))
  for i in P:
    j=BinarySearch(arr,0,len(R),i)
    cnt=0
    if j!=-1:
      while (not (arr[j][0]<=i<=arr[J][1])) and j<len(R):j+=1
      while (arr[j][0]<=i<=arr[J][1]) and j<len(R):
        j+=1;cnt+=1
      if cnt!=0:ans.append((i,cnt))
  return ans





