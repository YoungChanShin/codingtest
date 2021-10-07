from math import sqrt


def convert(num, base):
    answer = ""
    while num > 0:
        num, r = divmod(num, base)
        answer = str(r) + answer
    return answer


def mysplit(myString, letter):
    answer = []
    chunk = ""
    for s in myString:
        if s == letter:
            if chunk != "":
                answer.append(int(chunk))
            chunk = ""
        else:
            chunk += s
    if chunk != "":
        answer.append(int(chunk))
    return sorted(answer)


def findPrime(maxNum):
    answer = [0 for i in range(maxNum + 1)]
    answer[0] = 1
    answer[1] = 1
    for i in range(2, int(sqrt(maxNum)) + 1):
        if answer[i] == 0:
            for j in range(2, maxNum // i + 1):
                answer[i * j] = 1
    return answer


def solution(n, k):
    answer = 0
    data = mysplit(convert(n, k), "0")
    mem = findPrime(data[-1])
    for d in data:
        if mem[d] == 0:
            answer += 1
    return answer


n = 437674
k = 3

print(mysplit(convert(n, k), "0"))
# print(convert(1000000, 4))

# print(len(str(1212210202001)))
# print(findPrime(121221))
# 3310021000
print(solution(n, k))
