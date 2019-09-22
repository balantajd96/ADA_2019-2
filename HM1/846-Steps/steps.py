from sys import stdin
import time
import math
def steps(x,y):
	n=abs(y-x)
	if n==1 or n==0:
		ans=n
	else:
		tmp=n-(1/math.sqrt(n))
		ans=int(2*math.sqrt(tmp))
	return ans
def main():
	begin=time.time()
	tcnt=int(stdin.readline())
	while tcnt!=0:
		tok=stdin.readline().split()
		print(steps(int(tok[0]),int(tok[1])))
		tcnt-=1
	end=time.time()
	#print(end-begin)
main()