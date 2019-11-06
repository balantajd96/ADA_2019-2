import sys

def solution(T):
    """
    returns the latest valid time that can be 
    obtained from T, as a string in the format 
    "HH:MM".
    """
    T=list(T)
    if T[0]=="?":
        if T[1]!="?":
            num=int(T[1])
            if num<=3:
                T[0]="2"
            else:
                T[0]="1"
        else:
            T[0]="2"; T[1]="3"
    else:
        num=int(T[0])
        if num==0 or num==1:
            if T[1]=="?":
                T[1]="9"
        else:
            if T[1]=="?":
                T[1]="3"

    if T[3]=="?":
        T[3]="5"
    if T[4]=="?":
        T[4]="9"
        
    T="".join(T)
    return T


def main():
    time=["??:??",
          "0?:??",
          "??:?9",
          "2?:??"]
    for T in time:
        print(solution(T))
main()