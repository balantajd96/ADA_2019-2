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
    """
    compute the possible paths acording to mask
    and index
    """
    tmp=""
    paths=[]; i=0
    #print("--------")
    #print(mask)
    #print(goal)
    for i in range(len(mask)):
        if mask[i]==goal[index]:
            paths.append("{:03b}".format(i))
    return paths

def is_correct(string, path, index):
    """
    verify if the path selected is correct
    path: 3-bits string
    index: index to place path
    """
    ans=True
    print(string)
    print(path, index)

    cnt=-1
    for i in range(3):
        if string[index+cnt]=="2":
            string[index+cnt]=path[i]
        else:
            if string[index+cnt]!=path[i]:
                ans=False
        cnt+=1
    """
    if index==0:
        if string[-1]!="2":
            if string[-1]!=path[0]:
                ans=False
        else:
            string[-1]=path[0]
        
        if string[0]!="2":
            if string[0]!=path[1]:
                ans=False
        else:
            string[0]=path[1]

        if string[1]!="2":
            if string[1]!=path[2]:
                ans=False
        else:
            string[1]=path[2]

        
        string[-1]=path[0]
        string[0]=path[1]
        string[1]=path[2]
        
    elif 1<=index<=len(string)-2:
        if string[index-1]==path[0] and string[index]==path[1]:
            string[index+1]=path[1]
        else:
            ans=False
    else:
        if string[index-1]==path[0] and string[index]==path[1] and string[0]==path[2]:
           pass
        else:
            ans=False 
    """
    print(ans)
    print(string)
    return ans
def solve(goal, string, len_string, mask, index):
    ans=None
    if index==len(string):
        ans=True
        for i in range(len(string)):
            if  string[i]=="2":
                ans=False
    else:
        #print(goal, string, len_string, mask, index)
        _paths=paths(string, goal, index, mask)
        if _paths==[]:
            return True
        else:
            for i in range(len(_paths)):
                tmp=string
                if is_correct(string, _paths[i], index):
                    print("------------------------------------------------correcto")
                    ans=solve(goal, string, len_string, mask, index+1)
                else:
                    print("------------------------------------------------malo")
                    string=tmp
    return ans

def main():
    ok=True
    while ok:
            tmp=stdin.readline().split()
            if tmp!=[]:
                mask,len_string,goal=tmp[0],tmp[1],tmp[2]
                mask="{:08b}".format(int(mask))
                len_string=int(len_string)
                string=""
                for i in range(len_string): string+="2"
                answer=solve(goal, list(string), len_string, mask, 0)
                if answer:print("GARDEN OF EDEN")
                else:print("REACHABLE")
            else:
                ok=False    
main()