from sys import stdin,setrecursionlimit
setrecursionlimit(11000)

N,K,num = None,None,None

def phi(A,K,n,k,mem):
  ans=None
  if (n,k) in mem:
    ans=mem[(n,k)]
  else:  
    if n==0:
      ans=(k==0)
    else:
      ans=phi(A,K,n-1,(k+A[n-1])%K,mem) or phi(A,K,n-1,(k-A[n-1])%K,mem)
      mem[(n,k)]=ans
  return ans

def solve(A,K,n,mem):
  return phi(A,K,n,0,mem)

def main():
  global N,K,num
  tcnt = int(stdin.readline())
  while tcnt!=0:
    N,K = map(int, stdin.readline().split())
    mem=dict()
    num = list(map(int, stdin.readline().split()))
    print('Divisible' if solve(num,K,N,mem) else 'Not divisible')
    tcnt -= 1
main()
