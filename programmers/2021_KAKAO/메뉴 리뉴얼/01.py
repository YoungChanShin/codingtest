dictionary = dict()

def solution(orders, course):
    answer = []
    for i in range(11):
        dictionary[i] = dict()
    for o in orders:
        search(o, 0, "")
    for c in course:
        ret = sorted(dictionary[c].items(), key=lambda x:-x[1])
        if ret:
            max_val = ret[0][1]
            i = 0
            while max_val>1 and i < len(ret) and max_val == ret[i][1]:
                answer.append(ret[i][0])
                i+=1
    answer.sort()
    return answer

def search(order, cnt, arr):
    if cnt == len(order):
        l = "".join(sorted(arr))
        if l in dictionary[len(l)].keys():
            dictionary[len(l)][l] += 1
        else:
            dictionary[len(l)][l] = 1
        return
    search(order, cnt + 1, arr+order[cnt])
    search(order, cnt + 1, arr)



orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	
course = [2,3,5]
print(solution(orders, course))

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))



# print(dictionary)