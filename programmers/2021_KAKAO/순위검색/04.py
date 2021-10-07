from bisect import bisect_left

def solution(info, query):
    answer = []
    data = dict()
    for lang in ("cpp", "java", "python","-"):
        for pos in ("backend", "frontend","-"):
            for career in ("junior", "senior","-"):
                for food in ("chicken","pizza","-"):
                    data[(lang,pos,career,food)] = []
    for i in info:
        l,p,c,f,s = i.split()
        data[(l,p,c,f)].append(int(s))
        data[(l,p,c,"-")].append(int(s))
        data[(l,p,"-",f)].append(int(s))
        data[(l,p,"-","-")].append(int(s))

        data[(l,"-",c,f)].append(int(s))
        data[(l,"-",c,"-")].append(int(s))
        data[(l,"-","-",f)].append(int(s))
        data[(l,"-","-","-")].append(int(s))

        data[("-",p,c,f)].append(int(s))
        data[("-",p,c,"-")].append(int(s))
        data[("-",p,"-",f)].append(int(s))
        data[("-",p,"-","-")].append(int(s))

        data[("-","-",c,f)].append(int(s))
        data[("-","-",c,"-")].append(int(s))
        data[("-","-","-",f)].append(int(s))
        data[("-","-","-","-")].append(int(s))


n
    for q in query:
        cnt = 0
        l,p,c,fAnds = q.split(" and ")
        f,s = fAnds.split()
        s = int(s)
        list_ = data[(l,p,c,f)]
        answer.append(len(list_)-bisect_left(list_, s))
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))