langes = ["cpp", "java", "python"]
positions = ["backend", "frontend"]
careers = ["junior", "senior"]
foods = ["chicken", "pizza"]
# 점수는 코딩테스트 점수를 의미하며, 1 이상 100,000 이하인 자연수입니다.

def solution(info, query):
    answer = []
    volunteers = [[[[[] for w in range(2)] for z in range(2)] for y in range(2)] for x in range(3)]
    querys = []
    for i in info:
        l,p,c,f,s = i.split()
        if l == langes[0]:
            l = 0
        elif l == langes[1]:
            l = 1
        elif l == langes[2]:
            l = 2
        
        if p == positions[0]:
            p = 0
        elif p == positions[1]:
            p = 1
        
        if c == careers[0]:
            c = 0
        elif c == careers[1]:
            c = 1
        
        if f == foods[0]:
            f = 0
        elif f == foods[1]:
            f = 1
        volunteers[l][p][c][f].append(int(s))
# l,p,c,f
    for l in range(3):
        for p in range(2):
            for c in range(2):
                for f in range(2):
                    volunteers[l][p][c][f].sort()

    for v in volunteers:
        print(v)    
    for q in query:
        temp = q.split(' and ')
        t1,t2 = temp[3].split()
        querys.append((temp[0], temp[1], temp[2], t1,int(t2)))

    
    # 탐색
    for q in querys:
        cnt = 0
        ql,qp,qc,qf,qs = q
        for l in range(3):
            if ql=='-' or ql==langes[l]:
                for p in range(2):
                    if qp=='-' or qp==positions[p]:
                        for c in range(2):
                            if qc=='-' or qc==careers[c]:
                                for f in range(2):
                                    if qf=='-' or qf==foods[f]:
                                        n = len(volunteers[l][p][c][f])
                                        for i in range(n):
                                            if volunteers[l][p][c][f][i]>=qs:
                                                cnt += n-i
                                                break
                                                
        answer.append(cnt)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))