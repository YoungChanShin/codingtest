def solution(w, h):
    answer = 0
    g=0
    if w==h:
        g = w
    else:
        start = max(w,h)//2+1
        for i in range(start,0,-1):
            if w%i == 0 and h%i == 0:
                g = i
                break
    answer  = w*h - g*(w//g + h//g - 1)
    return answer

print(solution(4,4))