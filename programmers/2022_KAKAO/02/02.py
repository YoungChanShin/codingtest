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
    return answer


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    data = mysplit(convert(n, k), "0")
    for d in data:
        if isPrime(d):
            answer += 1
    return answer


n = 101010111
k = 10

print(solution(n, k))
print(isPrime(111))
print(111 // 3)
