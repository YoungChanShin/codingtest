def solution(id_list, report, k):
    answer = []
    report = set(report)
    print(id_list)
    report_from_to = {_from: set() for _from in id_list}
    times = {_from: 0 for _from in id_list}
    for re in report:
        _from, _to = re.split()
        report_from_to[_from].add(_to)
        times[_to] = times[_to] + 1
    stops = set()
    for user in times:
        if times[user] >= k:
            stops.add(user)
    print(report_from_to, times, stops)
    for user in report_from_to:
        answer.append(len(report_from_to[user] & stops))

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list, report, k))