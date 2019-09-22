from sys import stdin

def solve(text, p):
  ans,first,last = None,None,None
  return ans,first,last

def main():
  text = stdin.readline().strip()
  tcnt = int(stdin.readline())
  while tcnt!=0:
    p = stdin.readline().strip()
    ans,first,last = solve(text, p)
    if ans: print('Matched {0} {1}'.format(first, last))
    else: print('Not matched')
    tcnt -= 1

main()
