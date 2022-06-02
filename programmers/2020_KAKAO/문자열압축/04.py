def solution(s):
    l = 3
    for idx in range(l, len(s) + 1, l):
        print(s[idx : idx + l])
        print(len(s[idx : idx + l]))


s = "123456789012"

solution(s)