import sys
sys.setrecursionlimit(10002) 

MEMO=dict()
def solution(A, server_A, server_B, idx):
	global MEMO
	ans=10001
	if (sum(server_A), idx) in MEMO:
		ans=MEMO[(sum(server_A), idx)]
	else:
		if idx==len(A):
			ans=(min(ans, abs(sum(server_A)-sum(server_B))))
		else:
			tmp_A=list(server_A)
			tmp_A.append(A[idx])
			tmp_B=list(server_B)
			tmp_B.append(A[idx])
			ans=min(ans, solution(A, tmp_A, server_B, idx+1),
						solution(A, server_A, tmp_B, idx+1))
			MEMO[(sum(server_A), idx)]=ans
	return ans
  

def main():
	A=[4378,3121,8134,4542,5962,8835,2228,7314,1,2,3,65,4,8,5,1000,34,1,2,53,34,5676,1,2228,7314,1,2,3,65,4,8,5,1000]
	print(solution(A, [], [], 0))
main()