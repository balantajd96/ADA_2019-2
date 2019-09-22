def fib(n):
	assert 0 <= n
	ans = None 
	if n<=1:
		ans = n
	else:
		ans = fib(n - 2) + fib(n - 1)
	return ans

#now let's use memorization

def fib_dp(n, mem):
	assert 0 <= n
	ans =  None
	if mem[n]!=-1:ans=mem[n]
	else:
		if n<=1:
			ans = n
		else:
			ans = fib_dp(n-1, mem) + fib_dp(n-2, mem)
			mem[n] = ans
	return ans

a=[]
for i in range(10000):
	a.append(-1)

n=60
print(fib_dp(n,a))

while i<=mid and j<=hi: 
        if arr[i]<=arr[j]: 
            i+=1
        else: 
            cnt+=(mid-i+1) 
            j+=1

            