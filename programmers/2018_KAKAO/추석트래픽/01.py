lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

def convert(line):
    day, time, sustain = line.split()
    h,m,s = time.split(":")
    converted_s = int((float(h)*3600 + float(m)*60 +float(s))*1000)
    sustain = int(float(sustain.split("s")[0])*1000)
    start = converted_s-sustain+1
    end = converted_s

    return start, end

def isContain(time, line):
    # time부터 (0.999)초 동안 line과 겹치는 부분이 있는가
    time_post = time+999
    if line[0]<=time<=line[1] or line[0]<=time_post<=line[1] or time<=line[0]<=time_post or time<=line[1]<=time_post:
        return True
    return False 

def solution(lines):
    answer = 0
    connections = []
    for i in lines:
        connections.append(convert(i))
    
    for timeline in connections:
        start, end = timeline
        cnt_0, cnt_1,cnt_2, cnt_3 = 0, 0, 0, 0
        for line in connections:
            if isContain(start-999, line):
                cnt_0 += 1
            if isContain(start, line):
                cnt_1 += 1
            if isContain(end-999, line):
                cnt_2 += 1
            if isContain(end, line):
                cnt_3 += 1
            
        answer = max(answer, cnt_0, cnt_1, cnt_2, cnt_3)
    return answer
print(solution(lines))