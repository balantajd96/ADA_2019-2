from sys import stdin
import time

def solve(k):
  k=abs(k)  
  ans=0; tmp=0; i=1
  while (tmp<k):
    tmp=(i*(i+1))/2
    i+=1
  i-=1;tmp=1
  while (tmp%2!=0):
    tmp=((i*(i+1))/2)-k
    i+=1
  if i==0:
    ans=0
  elif k==0:
    ans=3
  else:
    ans=i-1
  return ans

def solve_2(k):
  k=abs(k)
  if k==0:
    ans=3
  elif k==1:
    ans=1
  else:
    ans=BinarySearchI(0,1000000000,k)
    while ((sum(ans)-k)%2)!=0:
      ans+=1


  return ans

def sum(x):
  return (x*(x+1))/2

def BinarySearchI(lo,hi,k):
  """
  Búsqueda binaria que encuentra el primer número
  mayor a k que cumpla la sumatoria
  """
  ans=-1
  mid=-1
  p=0
  while lo+1<hi:
    mid=(lo+hi)>>1
    suma=sum(mid)
    if suma==k:
      ans=mid
      lo=hi; p=1
    elif suma<k:
      lo=mid+1
    else:
      hi=mid

  if p!=1:
    if sum(lo)>k:
      ans=lo
    elif sum(hi)>k:
      ans=hi 
  return ans

def main():
  begin=time.time()
  tcnt,first = int(stdin.readline()),True
  i=0
  while tcnt!=0:
    stdin.readline()
    if first==False: print()
    first = False
    print(solve_2(int(stdin.readline())))
    tcnt -= 1
    i+=1
  end=time.time()
  #print(end-begin)
main()
