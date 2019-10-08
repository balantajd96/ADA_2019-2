from sys import stdin


def mic_wf(L,H,a):
  """
  Codigo de ADA-2019-1 
  Minimal Covering Algorithm with failure checking
  """
  a.sort()
  ans,low,n,ok,N = list(),L,0,True,len(a)
  cnt=len(a)
  while ok and low<H and n!=N:
    ok = a[n][0]<=low
    best,n = n,n+1
    while ok and n!=N and a[n][0]<=low:
      if a[n][1]>a[best][1]:
        best = n
      n += 1
    ans.append(best)
    cnt-=1
    low = a[best][1]
  ok = ok and low>=H
  if ok==False:
    ans = list()
  if ans==[]:cnt=-1
  return cnt


def solve(L,arr):
    candidates=[]
    for i in range(len(arr)):
      lo=arr[i][0]-arr[i][1]
      hi=arr[i][0]+arr[i][1]
      candidates.append((lo,hi))
    ans=mic_wf(0,L,candidates)
    return ans


def main():
    tmp=True
    while tmp:
      L,G=map(int, stdin.readline().split())
      if not (L==0 and G==0):
        arr=[]
        for i in range(G):
            pos,r=map(int, stdin.readline().split())
            arr.append((pos,r))
        print(solve(L,arr))
      else:
        tmp=False           
main()
