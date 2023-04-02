import sys

sys.stdin = open("input.txt")

S = input()
answer = [0 for i in range(26)]

for l in S:
    answer[ord(l)-ord('a')] += 1

for c in answer:
    print(c, end=' ')
# print(ord("a"))
# print(answer)