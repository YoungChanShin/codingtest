import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
answer = [0 for _ in range(26)]
for _ in range(N):
    name = input()[0]
    answer[ord(name)-ord('a')] += 1

ret = ""
for i in range(26):
    if answer[i]>4:
        ret += chr(i+ord('a'))
if len(ret) == 0:
    ret = 'PREDAJA'
print(ret)
