from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    dist.sort(reverse=True)
    candidate = list(permutations(weak, min(len(weak), len(dist))))  # 시작점

    for sp in candidate:
        checkList = {
            weak[w]: [False, weak[(w + 1) % len(weak)]] for w in range(len(weak))
        }

        def isComplete():
            for w in checkList:
                if not checkList[w][0]:
                    return False
            return True

        cnt = 0
        for pidx, p in enumerate(sp):
            cnt += 1
            tp = p
            broad = dist[pidx]
            while broad > -1:
                checkList[tp][0] = True
                newTp = checkList[tp][1]
                broad -= (newTp - tp) % n
                tp = newTp
            if isComplete():
                print(cnt)
                if answer > cnt:
                    answer = cnt
                break
    if answer == len(dist) + 1:
        answer = -1
    return answer


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))