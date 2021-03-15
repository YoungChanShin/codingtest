def compress(word_len, s):
    ret = ""
    cnt = 1
    for i in range(0,len(s), word_len):
        start = s[i:i+word_len]
        if start == s[i+word_len:i+word_len+word_len]:
            cnt += 1
        else:
            if cnt > 1:
                ret = ret + str(cnt) + start
                cnt = 1
            else:
                ret = ret + start
    return ret



def solution(s):
    if len(s) == 1:
        return 1
    answer = 1001
    for i in range(1, len(s)//2+1):
        answer = min(answer, len(compress(i,s)))
    return answer

ss = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd", "a"]
for s in ss:
    print(solution(s))