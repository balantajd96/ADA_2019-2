from sys import stdin
import time

def solve(RAE,big_cad, mini_cad):
	ans,first,last = None,None,None
	#RAE=Dic(big_cad)
	ans=[0,0]
	tmp=-1; index=0; i=0
	while index!=-1 and i<len(mini_cad):
		ch=mini_cad[i] #letra a buscar
		h=RAE[ch]  #lista de indices de la letra ch
		index=BinarySearchI(h,0,len(h)-1,tmp)
		#se pasa tmp porque ese es el índice actual
		#que se puede usar
		if index!=-1:
			if i==0: first=index
			if i==len(mini_cad)-1: last=index
			ans=True
			tmp=index
		else:
			ans=False
		i+=1
	return ans,first,last

def Dic(big_cad):
	"""
	Recibe una cadena de caracteres  y restorna un diccionario
	separados por las letras del alfabeto de manera acendente
	guardando sus índices correspondientes a la cadena de entrada
	"""
	dic={'a':[],'b':[],'c':[],'d':[],'e':[],
		 'f':[],'g':[],'h':[],'i':[],'j':[],
		 'k':[],'l':[],'m':[],'n':[],'o':[],
		 'p':[],'q':[],'r':[],'s':[],'t':[],
		 'u':[],'v':[],'w':[],'x':[],'y':[],'z':[],
		 'A':[],'B':[],'C':[],'D':[],'E':[],
		 'F':[],'G':[],'H':[],'I':[],'J':[],
		 'K':[],'L':[],'M':[],'N':[],'O':[],
		 'P':[],'Q':[],'R':[],'S':[],'T':[],
		 'U':[],'V':[],'W':[],'X':[],'Y':[],'Z':[]}

	l_cad=list(big_cad)
	for i in range(len(l_cad)):
		key=l_cad[i]
		list_tmp=dic.get(key)
		list_tmp.append(i)
		dic[key]=list_tmp
	return dic

def BinarySearchI(A, lo, hi, x):
	"""
	Búsqueda binaria que encuentra el primer número
	mayor a x
	"""
	ans=-1
	if lo==hi:
		if A[lo]>x:
			ans=A[lo]
	elif len(A)!=0:
		while lo+1<hi:
			mid=(lo+hi)>>1
			if A[mid]<=x:
				lo=mid+1
			else:
				hi=mid
		if A[lo]>x:
			ans=A[lo]
		elif A[hi]>x:
			ans=A[hi]
	return ans

def main():
  begin=time.time()
  text = stdin.readline().strip()
  tcnt = int(stdin.readline())
  RAE=Dic(text)
  while tcnt!=0:
    p = stdin.readline().strip()
    ans,first,last = solve(RAE,text, p)
    if ans: print('Matched {0} {1}'.format(first, last))
    else: print('Not matched')
    tcnt -= 1
  end=time.time()
  #print(end-begin)

main()