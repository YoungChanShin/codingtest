import sys
sys.stdin = open('input.txt', 'r')

S = input()
N =len(S)//2
def isPalindrome(S):
    for i in range(N):
        if S[-1-i] != S[i]:
            return False
    return True
print(int(isPalindrome(S)))
    