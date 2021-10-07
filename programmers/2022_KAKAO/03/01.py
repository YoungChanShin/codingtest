def convert(time_to_min):
    hh, mm = time_to_min.split(":")
    return int(hh) * 60 + int(mm)


def calc(fees, time):
    basic_time, basic_fee, unit_time, unit_fee = fees
    if time <= basic_time:
        return basic_fee
    return basic_fee + (time - basic_time + unit_time - 1) // unit_time * unit_fee


def solution(fees, records):
    answer = []
    stat = dict()
    for car in records:
        t, c, s = car.split()
        t = convert(t)
        if c not in stat.keys():
            stat[c] = [True, t, 0]  # 주차장에 in, 입차 시간, 누적 시간
        else:
            if s == "IN":
                stat[c] = [True, t, stat[c][2]]  # 재입차
            else:
                stat[c] = [False, t, stat[c][2] + t - stat[c][1]]

    for car in stat:
        if stat[car][0]:
            stat[car] = [False, t, stat[car][2] + convert("23:59") - stat[car][1]]
        answer.append((car, calc(fees, stat[car][2])))
    answer = [car[1] for car in sorted(answer)]
    return answer


fee = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]

print(solution(fee, records))