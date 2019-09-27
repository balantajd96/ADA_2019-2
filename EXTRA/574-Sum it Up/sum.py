from sys import stdin
ans=[]
def solve4(arr, num, tmp, index):
	tmp.reverse()
	if num==0 and not (tmp in ans):
		ans.append(tmp)
	elif index<len(arr):
		if num-arr[index]>=0:
			solve4(arr,num-arr[index],tmp+[arr[index]],index+1)
			solve4(arr,num,tmp,index+1)

def main():
  global t,lst,ans 	
  line = list(map(int,stdin.readline().split()))
  while line[1]!=0:
    t,n,lst = line[0],line[1],line[2:len(line)]
    lst=lst[::-1]
    solve4(lst,t,[],0) 
    print("Sums of {}:".format(t))
    ans.sort()
    ans=ans[::-1]
    if len(ans)!=0: 
      for op in ans: 
        print(op[0],end="")
        for i in range(1,len(op)): print("+",end="{}".format(op[i]))
        print()
    else: print("NONE")
    line = list(map(int,stdin.readline().split()))
    ans=[]
  return
main()