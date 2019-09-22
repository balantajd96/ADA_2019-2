from sys import stdin,setrecursionlimit
setrecursionlimit(11000)

N,K,num = None,None,None

def solve():
  pass

def main():
  global N,K,num
  tcnt = int(stdin.readline())
  while tcnt!=0:
    N,K = map(int, stdin.readline().split())
    num = list(map(int, stdin.readline().split()))
    print('Divisible' if solve() else 'Not divisible')
    tcnt -= 1

main()
