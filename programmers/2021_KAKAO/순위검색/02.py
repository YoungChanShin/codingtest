langes = ["cpp", "java", "python","-"]
positions = ["backend", "frontend","-"]
careers = ["junior", "senior","-"]
foods = ["chicken", "pizza","-"]
# 점수는 코딩테스트 점수를 의미하며, 1 이상 100,000 이하인 자연수입니다.

def solution(info, query):
    answer = []
    volunteers = [[[[[] for w in range(3)] for z in range(3)] for y in range(3)] for x in range(4)]
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
        s = int(s)
        volunteers[l][p][c][f].append(s)
        volunteers[l][p][c][2].append(s)
        volunteers[l][p][2][f].append(s)
        volunteers[l][p][2][2].append(s)
        
        volunteers[l][2][c][f].append(s)
        volunteers[l][2][c][2].append(s)
        volunteers[l][2][2][f].append(s)
        volunteers[l][2][2][2].append(s)

        volunteers[3][p][c][f].append(s)
        volunteers[3][p][c][2].append(s)
        volunteers[3][p][2][f].append(s)
        volunteers[3][p][2][2].append(s)

        volunteers[3][2][c][f].append(s)
        volunteers[3][2][c][2].append(s)
        volunteers[3][2][2][f].append(s)
        volunteers[3][2][2][2].append(s)

    # for v in volunteers:
    #     print(v)    
    for q in query:
        temp = q.split(' and ')
        t1,t2 = temp[3].split()
        querys.append((temp[0], temp[1], temp[2], t1, int(t2)))

    
    # 탐색
    for q in querys:
        cnt = 0
        ql,qp,qc,qf,qs = q
        for l in range(4):
            if ql==langes[l]:
                ql = l
                break
        for p in range(3):
            if qp==positions[p]:
                qp = p
                break
        for c in range(3):
            if qc==careers[c]:
                qc = c
                break
        for f in range(3):
            if qf==foods[f]:
                qf = f
                arr = volunteers[ql][qp][qc][qf]
                break
        arr.sort()
        n = len(arr)
        for i in range(n):
            if arr[i]>=qs:
                cnt += n-i
                break
        answer.append(cnt)
                                                
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))