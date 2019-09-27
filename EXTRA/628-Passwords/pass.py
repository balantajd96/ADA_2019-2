from sys import stdin
ans=""
def solve2(words, rules, index):
	global ans
	if index!=len(rules):
		if rules[index]=="#":
			for i in range(len(words)):
				tmp=ans
				ans=ans+words[i]
				solve2(words, rules, index+1)
				ans=tmp
		else:
			for i in range(10):
				ans=ans+str(i)
				solve2(words, rules, index+1)
				ans=ans[0:len(ans)-1]
	else:
		print(ans)

def main():
	global ans
	ok=True
	while ok:
		word_cnt = stdin.readline()
		if len(word_cnt)!=0:
			word_cnt = int(word_cnt)
			words=[]; rules=[]
			for i in range(word_cnt):
				tmp=stdin.readline()
				tmp=tmp[0:len(tmp)-1]
				words.append(tmp)
			rules_cnt = int(stdin.readline())
			for i in range(rules_cnt):
				tmp=stdin.readline()
				if tmp[-1]=="\n":
					tmp=tmp[0:len(tmp)-1]
				rules.append(tmp)
			
			print("--")
			for i in range(len(rules)):				
				solve2(words, rules[i], 0)
			
			ans=""
			#print(words)
			#print(rules)
		else:
			ok=False
		
main()