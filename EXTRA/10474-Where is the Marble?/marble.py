from sys import stdin

def binarySearch(l, x):
    """
    l: list of ordered numbers
    x: number to find
    """
    ans=-1
    lo,hi=0,len(l)-1
    while lo+1<hi:
        mid=(lo+hi)>>1
        if x<=l[mid]:
            hi=mid
        else:
            lo=mid+1
    if l[lo]==x:
        ans=lo+1
    elif l[hi]==x:
        ans=hi+1
    return ans


def solve(marbles, queries):
    ans=[]
    marbles.sort()
    for num in queries:
        ans.append((num, binarySearch(marbles, num)))
    return ans


def main():
    ok=True
    cnt=1
    while ok:
        N,Q=map(int,stdin.readline().split())
        if N==0 and Q==0:
            ok=False
        else:
            marbles,queries=[],[]
            for _ in range(N):
                marbles.append(int(stdin.readline()))
            for _ in range(Q):
                queries.append(int(stdin.readline()))
            
            ans=solve(marbles,queries)
            print("CASE# {0}:".format(cnt))
            for num in ans:
                if num[1]==-1:
                    print("{0} not found".format(num[0]))
                else:
                    print("{0} found at {1}".format(num[0], num[1]))
            cnt+=1
main()