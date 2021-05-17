def trans(arr):
    n = len(arr)
    ret = [[0]*n for j in range(n)]
    for i in range(n):
        binary = format(arr[i],'b')
        b_len = len(binary)
        for j in range(len(binary)):
            ret[i][n-len(binary)+j] = int(binary[j])
    return ret

def solution(n, arr1, arr2):
    answer = ['' for _ in range(n)]
    first = trans(arr1)
    second = trans(arr2)
    for i in range(n):
        for j in range(n):
            if first[i][j]==1 or second[i][j]==1:
                answer[i] = '#' + answer[i]
            else:
                answer[i] = ' ' + answer[i]
    for i in range(n):
        answer[i] = ''.join(answer[i])
    return answer

print(list('asdf'))


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n,arr1, arr2))