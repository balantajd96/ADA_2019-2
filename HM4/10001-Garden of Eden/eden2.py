from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)


paths=[]
answer=None
def solve(goal, string, len_string, mask, index):
    global paths, answer
    if index==len(string)-1:
        #print("")
        #print("")
        #print("----------------------------------------------Verificando")
        #Se verifica que la cadena final sea correcta
        bit_goal=goal[len_string-1]
        arr=[]
        print(goal, string)
        for i in range(8):
            tmp="{:03b}".format(i)
            if tmp[1]==bit_goal:
                arr.append(list(tmp))

        print(arr)
        for i in range(len(arr)):
            print(string[len_string-2],string[len_string-1],string[0],arr[i])
            if string[len_string-2]==arr[i][0] and string[len_string-1]==arr[i][1] and string[0]==arr[i][1]:
                print("TRUE")
                answer=True
        return
    else:
        for i in range(8):
            path=paths[i]
            #print("Inicio")
            #print(string, index, mask)
            if string[index]==mask[i]:
                #print("Aqui")
                if string[index-1]==path[0] and string[index]==path[1]:
                    string[index+1]=path[2]
                    solve(goal, string, len_string, mask, index+1)
                """
                if string[index-1]==path[0] and string[index]==path[1]:
                    print("Aca")
                    if string[index+1]=="2" or (string[index+1]==path[2]):
                        print("Alla")
                        string[index-1]=path[0]
                        string[index]=path[1]
                        string[index+1]=path[2]
                        solve(goal, string, len_string, mask, index+1)   
                """
#True: garden
#False: reachable
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
                mask2=mask[::-1]

                string=[]
                for i in range(len_string): string.append("2")

                for i in range(8):
                    path=paths[i]
                    string[-1]=path[0]
                    string[0]=path[1]
                    string[1]=path[2]
                    solve(goal, list(string), len_string, mask, 1)
                    if answer:break
                    #print(answer, "----")

                if answer:print("REACHABLE")
                else:print("GARDEN OF EDEN")
                print("\n",answer,"\n\n\n")
            else:
                ok=False    
main()