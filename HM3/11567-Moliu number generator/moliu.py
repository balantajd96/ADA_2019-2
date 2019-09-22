from sys import stdin
def solve(n):
	"""
	n: número que voy a dividir por 2, sumar o restar 1
	La idea es siempre que se pueda dividir por 2
	si no se puede, se debe buscar que es mejor, sumar 1
	o restar 1. Después se sigue dividiendo por dos porque
	es la manera más rápida de acabar
	"""
	cnt=0
	while(n!=0):
		if (n%2==0):n=n//2
		else:
			if n==1:n=0
			elif n==2:n=1
			elif n==3:n=2
			else:
				tmp1=n+1; tmp2=n-1; maxi=0
				while(tmp1%2==0 and tmp1!=0):
					tmp1=tmp1//2
					maxi+=1
				while(tmp2%2==0 and tmp2!=0):
					tmp2=tmp2//2
					maxi-=1
				if maxi>0:n+=1
				else:n-=1
		cnt+=1
	return cnt

def main():
	tmp=True
	while tmp:
		n=stdin.readline()
		if n=="":
			tmp=False
		else:
			n=int(n)
			print(solve(n))

main()
