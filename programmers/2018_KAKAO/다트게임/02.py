def solution(dartResult):
    temp = 0
    result = 0

    for i in range(len(dartResult)):
        i_ = answer[i]
        if i_ == 'S':
            temp = temp
        elif i_ == 'D':
            temp = temp * temp
        elif i_ == 'T':
            temp = temp * temp * temp
        elif i_ == '*':
            result += temp
            result = result * 2
        elif i_ == '#':
            temp = -temp
            result += temp
        else:
            # 10일 경우
            if int(i_) == 0:
                temp = 10
            else:
                temp = int(i_)
        if i != 0:
            result += temp

    return result


# 37
print(solution('1S2D*3T'))
# -4
# print(solution('1T2D3D#'))
# 59
# print(solution('1D2S3T*'))