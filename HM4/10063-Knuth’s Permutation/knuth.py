from sys import stdin

#help https://amrfeldfrawy.wordpress.com/2013/07/11/uva-10063-knuths-permutation/
def solve(string, index, word):
	if index==len(word):
		print(string)
	else:
		c=word[index]
		for i in range(len(string)+1):
			tmp=string
			tmp=tmp[:i]+c+tmp[i:]
			solve(tmp, index+1, word)


def main():
	ok=True
	while ok:
		word=stdin.readline().split()
		if word==[]:
			ok=False
		else:
			solve(word[0][0], 1, word[0])
			print("")
main()
