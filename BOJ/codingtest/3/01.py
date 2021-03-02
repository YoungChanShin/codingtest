# pickup = [0,2,9,10,11,12]
# drop = [5,9,11,11,14,17]
# tip = [1,2,3,2,2,1]

# pickup = [4,1]
# drop = [6,5]
# tip = [5,2]

pickup = [11,30,0,21,41,19]
drop = [20,31,17,22,46,21]
tip = [6,1,9,0,8,0]

def solution(cnt, location):
    N = len(pickup)
    profit = 0
    if location > drop[-1]:
        return 0

    for i in range(cnt, N):
        if location <= pickup[i]:
            new_location = drop[i]
            profit = max(profit, solution(i, new_location)+drop[i]-pickup[i]+tip[i])
    return profit


def taxi(pickup, drop, tip):
    print(solution(0, 0))

listsum = zip(pickup, drop, tip)
new_list = sorted(listsum, key=lambda x:x[0])
pickup, drop, tip = zip(*new_list)


taxi(pickup, drop, tip)