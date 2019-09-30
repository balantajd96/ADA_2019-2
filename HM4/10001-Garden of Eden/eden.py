from sys import stdin
paths=[]
answer=None
#Help from: 
#    https://blog.csdn.net/helloworld10086/article/details/38589723
#    https://blog.csdn.net/primoblog/article/details/8614007
#    David Hernández, Nicolás Ortiz, Edixon Arias
def solve(string, len_string, goal, mask, index):
    global paths, answer
    if index==len_string:   
        #Verify if last insertion is correct
        if string[0]==string[len_string] and string[1]==string[len_string+1]: answer=True
        return
    else:
        for i in range(8):
            if not mask[i]!=goal[index]:
                if index!=0:    
                    #Check if new bits can be inserted without damaging the previous ones
                    if string[index]==paths[i][0] and string[index+1]==paths[i][1]:
                        string[index+2]=paths[i][2]
                        solve(string, len_string, goal, mask, index+1)                    
                else:   
                    #First iteration, can insert without problems
                    string[0]=paths[i][0]; string[1]=paths[i][1]; string[2]=paths[i][2]
                    solve(string, len_string, goal, mask, index+1)
                    
def main():
    global paths, answer
    ok=True
    for i in range(8):
        tmp="{:03b}".format(i)
        paths.append(list(tmp))
    while ok:
            answer=False
            tmp=stdin.readline().split()
            if tmp!=[]:
                mask,len_string,goal=tmp[0],int(tmp[1]),tmp[2]

                mask="{:08b}".format(int(mask))
                mask=mask[::-1]

                string=[]
                for i in range(len_string+2): string.append("2")
                solve(string, len_string, goal, mask, 0)
                if answer:print("REACHABLE")
                else:print("GARDEN OF EDEN")
            else:
                ok=False    
main()