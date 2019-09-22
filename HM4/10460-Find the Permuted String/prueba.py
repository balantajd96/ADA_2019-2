import math
def string_insert(string, index, c):
	"""
	insert "c" char into string in index position
	"""
	assert 0<=index<=len(string)
	ans=""; i=0; tmp=0
	while i<=len(string):
		if i==index:
			ans=ans+c
			tmp=1
		else:
			ans=ans+string[i-tmp]
		i+=1
	return ans

def solve(string, index):
	ans=string[0]
	tree_level=1
	lo=1
	hi=math.factorial(len(string))
	while total!=1:
		mid=(lo+hi)>>1

"""
test="ACB"
i=2
c="X"
print(string_insert(test,i,c))
"""
test="ACB"
i=5
solve(test,i)