from sys import stdin

def solve(k):
  ans = 0
  # your code goes here
  return ans

def main():
  tcnt,first = int(stdin.readline()),True
  while tcnt!=0:
    stdin.readline()
    if first==False: print()
    first = False
    print(solve(int(stdin.readline())))
    tcnt -= 1

main()
