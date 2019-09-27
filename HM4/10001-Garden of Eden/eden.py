from sys import stdin
"""
def transform(bina,lent,mask):
    ans=''
    for i in range(lent):
        tmp="0b"
        if i==0:
            tmp+=bina[-1]+bina[0]+bina[1]
        elif 1<=i<=lent-2:
            tmp+=bina[i-1]+bina[i]+bina[i+1]
        else:
            tmp+=bina[i-1]+bina[i]+bina[0]
        ans+=mask[int(tmp,2)]
    return ans

def eden(target,lent,mask):
    ans=False
    cnt,bincnt=0,0
    while not ans and cnt<2**lent:
        bincnt=("{:0"+str(lent)+"b}").format(cnt)
        tmp=transform(bincnt,lent,mask)
        if tmp==target: ans=True
        cnt+=1
    return ans

def main():
    num=list(map(str, stdin.readline().split()))
    while num!=[]:
        if num!=[]:
            mask="{:08b}".format(int(num[0]))
            if eden(num[2],int(num[1]),mask): print('REACHABLE')
            else: print('GARDEN OF EDEN')
        num=list(map(str, stdin.readline().split()))
main()
"""
def paths(string, goal, index, mask):
    tmp=""
    paths=[]; i=0
    print("--------")
    print(mask)
    print(goal)
    for i in range(len(mask)):
        if mask[i]==goal[index]:
            paths.append("{:03b}".format(i))
    return paths

def is_correct(string, path, index):
    #Revisar
    ans=True
    if index==0:
        if string[-1]==2 and string[0]==2 and string[1]==2:
            string[-1]=path[0]
            string[0]=path[0] 
            string[1]=path[0]
    elif 1<=i<=lent-2:
        if string[i-1]==2 and string[i]==2 and string[i+1]==2:
            string[i-1]=path[0]
            string[i]=path[0] 
            string[i+1]=path[0]
    else:
        if string[i-1]==2 and string[i]==2 and string[0]==2:
            string[i-1]=path[0]
            string[i]=path[0] 
            string[0]=path[0]

def solve(goal, string, len_string, mask, index):
    ans=None
    if index==len(string):
        ans=True
        for i in range(len(string)):
            if  string[i]=="2":ans=False
    else:
        print(goal, string, len_string, mask, index)
        _paths=paths(string, goal, index, mask)
        for i in range(len(_paths)):
            tmp=string
            if is_correct(string, _paths[i], index):
                solve(goal, string, len_string, mask, index+1)
            else:
                string=tmp



    return ans

def main():
    goal="10101"
    len_string=len(goal)
    string=""
    mask="{:08b}".format(204)
    for i in range(len_string): string+="2"

    print(solve(goal, string, len_string, mask, 0))

main()