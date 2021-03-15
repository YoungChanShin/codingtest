def solution(food_times, k):
    answer = 0
    n = len(food_times)
    fd = dict()
    for i in range(n):
        try:    
            fd[food_times[i]].append(i)
        except:
            fd[food_times[i]] = [i]
    food_times.sort()
    height = 0
    print(fd)
    for i in range(n-1):
        if food_times[i] != food_times[i+1]:
            while k > 0 and height<= food_times[i]:
                k -= n-i
                height += 1
            if k > 0:
                continue
            if k == 0:
                print(food_times[i])
                return fd[food_times[i]][0]
            if k < 0:
                k += n-i
                return fd[food_times[i+k]]

    return answer

food_times = [3, 1, 2]
k = 3
print(solution(food_times, k))