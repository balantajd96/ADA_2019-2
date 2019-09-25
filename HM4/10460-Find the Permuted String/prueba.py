import math
def solve(string, index):
	ans=""
	n=len(string); h=0
	rang=(1,math.factorial(n))
	
	while h<n-1:
		div=(rang[0]+rang[1])//(h+1)
		path=[]
		lo=rang[0]
		ok=True; i=0
		while ok and i<h+1:
			path=(lo,lo+div-1)
			if path[0]<=index<=path[1]:
				ans=ans[:i]+string[h]+ans[i:]
				rang=(path[0],path[1])
				ok=False
			else:
				lo=lo+div
				i+=1
		h+=1
	#print(index, rang[0])
	#ans=string_insert(ans,index-rang[0],string[-1])
	ans=ans[:index-rang[0]]+string[h]+ans[index-rang[0]:]
	print(index,ans)
	#print("--------------------------------")

def solve2(string, index):
	ans=None
	n=len(string); h=2
	rang=(1,math.factorial(n))
	mid=((rang[0]+rang[1])//2)

	lo=1
	if index<=mid:
		ans=string[1]+string[0]
		ran=(1,mid)
	else:
		ans=string[0]+string[1]
		lo+=mid
		ran=(mid+1,n)
	
	while h<n-1:
		ok=True
		div=(rang[0]+rang[1])//(h+1)
		while ok:
			if lo<=index<=lo+div:
				ans=ans[:i]+string[h]+ans[i:]
				rang=(lo,lo+div)
				ok=False
		h+=1
	print(ans)





"""
test="ACB"
i=2
c="X"
print(string_insert(test,i,c))
"""
test="ACBF"
for i in range(24):solve2(test,i+1)
#i=4
#solve(test,i)