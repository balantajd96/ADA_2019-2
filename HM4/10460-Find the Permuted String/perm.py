from sys import stdin
import math
def generator(h,rang):
	"""generate all possibles paths from h to next level"""
	div=(rang[1]-rang[0])//(h+1)
	tmp=rang[0]
	ans=[]
	for i in range(h+1):
		ans.append((tmp,tmp+div))
		tmp+=div+1
	return ans

def solve4(string, index):
	ans=string[0]
	n=len(string)	#tree high
	ranges=(1,math.factorial(n))
	h=1
	while h!=n-1:
		range_level=generator(h,ranges)
		i=0; ok=False
		while ok==False:	#find correct path
			if range_level[i][0]<=index<=range_level[i][1]:
				ranges=(range_level[i][0],range_level[i][1])
				ans=ans[:i]+string[h]+ans[i:]
				ok=True
			i+=1
		h+=1
	ans=ans[:index-ranges[0]]+string[h]+ans[index-ranges[0]:]
	return ans

def main():
	cnt=int(stdin.readline())
	while cnt!=0:
		string=stdin.readline().strip()
		index=int(stdin.readline())
		print(solve4(string,index))
		cnt-=1
main()