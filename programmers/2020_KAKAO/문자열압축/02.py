def compress(word_len, s):
    ret = 0
    cnt = 1
    for i in range(0,len(s), word_len):
        start = s[i:i+word_len]
        if start == s[i+word_len:i+2*word_len]:
            cnt += 1
        else:
            if cnt > 1:
                ret += len(str(cnt)) + word_len
                cnt = 1
            else:
                ret += word_len
    return ret



def solution(s):
    if len(s) == 1:
        return 1
    answer = 1001
    for i in range(1, len(s)//2+1):
        answer = min(answer, compress(i,s))
    return answer

ss = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd", "a"]
for s in ss:
    print(solution(s))