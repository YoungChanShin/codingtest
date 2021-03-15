class Node:
    pass

def solution(words, queries):
    answer = []
    trie =[[] for _ in range(10001)]
    reversed_trie = [[] for _ in range(10001)]
    for w in words:
        trie[len(w)].append(w)
        reversed_trie[len(w)].append(w[::-1])
    for q in queries:
        cnt = 0
        N = len(q)
        if q[0] == '?':
            q = q[::-1].replace("?","")
            for w in reversed_trie[N]:
                if q == w[:len(q)]:
                    cnt += 1
        else:
            q = q.replace("?","")
            for w in trie[N]:
                if q == w[:len(q)]:
                    cnt += 1
        answer.append(cnt)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words,queries))