INF=float("inf")
def solve(arr1, arr2, num):
    """
    Find a pair of numbers from arr1 and arr2
    that the sum of them is the closest to
    num
    """
    arr1.sort(); arr2.sort()
    row=0; col=len(arr1)-1
    ok=False #stops if sum(pair)==num
    ans=(-1,-1); maxi=INF

    while col!=-1 and row!=len(arr1) and not(ok):
        summ=arr1[col]+arr2[row]
        if summ==num:
            ans=(arr1[col], arr2[row])
            ok=True
        else:
            if abs(summ-num)<maxi:
                ans=(arr1[col], arr2[row])
                maxi=summ
            if summ>num: col-=1
            else: row+=1
    return ans

def main():
    arr1=[6,-1,4,10]
    arr2=[0,2,1,6]
    num=8
    print("The closest numbers are:", solve(arr1, arr2, num))
main()