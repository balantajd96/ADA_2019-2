from sys import stdin
import time
import math
def step(x,y):
	n=abs(y-x)
	if n==1:
		ans=1
	else:
		ans=int(2*math.sqrt(n))
	return ans
def main():
	begin=time.time()
	tcnt=int(stdin.readline())
	while tcnt!=0:
		tok=stdin.readline().split()
		print(steps_crack(int(tok[0]),int(tok[1])))
		#print("******")
		tcnt-=1
	end=time.time()
	print(end-begin)
main()


def steps_bueno_pero_lento(x,y):
	ans=0
	n=abs(y-x) #n:distancia entre x & y
	i=3   #Inicio de un bloque doble
	pasos=3
	m=2   #multiplicador de los bloques
	lo=3; hi=lo+(m*2)-1
	if n==1 or n==2:
		pasos=n
	else:
		while n<lo or n>hi:
			m+=1
			pasos+=2
			lo=hi+1
			hi=lo+(m*2)-1
		mid=((lo+hi)>>1)+1
		if n>=mid:
			pasos+=1	
	return pasos