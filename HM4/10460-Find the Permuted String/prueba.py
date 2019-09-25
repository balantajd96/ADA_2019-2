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


def solve3(string, index):
	ans=string[0]
	n=len(string)	#tree high
	ranges=(1,math.factorial(n))
	h=1

	while h!=n-1:
		#print(ranges)
		div=(ranges[0]+ranges[1])//(h+1)
		i=0; ok=True; lo=ranges[0] #ok: path founded
		
		tmp=[]
		for i in range(h+1):
			tmp.append((lo,lo+div-1))
			lo+=div
		#print(ranges)
		#print(h,tmp)

		for i in range(len(tmp)):
			lo=tmp[i][0]; hi=tmp[i][1]
			if lo<=index<=hi:
				ranges=(lo,hi)
				ans=ans[:i]+string[h]+ans[i:]
				break
		print(div, ranges)
			

		
		"""
		while i!=h+1 and ok:	#number of paths
			#print("------------>",index)
			if lo<=index<=lo+div-1:
				print("Entre", lo, lo+div-1)
				ranges=(lo,lo+div-1); ok=False
				ans=ans[:i]+string[h]+ans[i:]
			else:
				lo+=div
			i+=1
		"""
		h+=1
		
	#print("-->",ans,h,string[h])
	ans=ans[:index-ranges[0]]+string[h]+ans[index-ranges[0]:]
	print(ans)


"""
test="ACB"
i=2
c="X"
print(string_insert(test,i,c))
"""
test="ABCF"
#for i in range(6):solve3(test,i+1)
print(solve3(test, 22))	#BCEADF
#i=4
#solve(test,i)
