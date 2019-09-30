import math
from sys import stdin
def ranges(pos,w_med,r):
    tmp=math.sqrt(r**2-(w_med)**2)
    return (pos-tmp,pos+tmp)

def mic_wf(L,H,a):
  """
  Codigo de ADA-2019-1 
  Minimal Covering Algorithm with failure checking
  """
  a.sort()
  ans,low,n,ok,N = list(),L,0,True,len(a)
  cnt=0
  while ok and low<H and n!=N:
    ok = a[n][0]<=low
    best,n = n,n+1
    while ok and n!=N and a[n][0]<=low:
      if a[n][1]>a[best][1]:
        best = n
      n += 1
    ans.append(best)
    cnt+=1
    low = a[best][1]
  ok = ok and low>=H
  if ok==False:
    ans = list()
  if ans==[]:cnt=-1
  return cnt

def solve(N,l,w,arr):
    candidates=[]
    for i in range(N):
        w_med=w/2
        if arr[i][1]>=(w_med):
            candidates.append(ranges(arr[i][0],w_med,arr[i][1]))
    ans=mic_wf(0,l,candidates)
    return ans

def main():
    tmp=True
    while tmp:
        try:
            N,l,w=map(int, stdin.readline().split())
            arr=[]
            for i in range(N):
                pos,r=map(int, stdin.readline().split())
                arr.append((pos,r))
            print(solve(N,l,w,arr))
        except:
            tmp=False           
main()
