from sys import stdin

def solve(x, y):
  ans = 0
  # your code goes here ...
  return ans

def main():
  tcnt = int(stdin.readline())
  while tcnt!=0:
    tok = stdin.readline().split()
    print(solve(int(tok[0]), int(tok[1])))
    tcnt -= 1

main()
