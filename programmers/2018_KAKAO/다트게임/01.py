def calc_bonus(bonus, score):
    if bonus == 'S':
        return score
    if bonus == 'D':
        return score**2
    return score**3

def calc_option(prev_score, cur_score, option):
    if option == '#':
        cur_score *= -1
    if option == '*':
        cur_score *= 2
        prev_score *= 2

    return prev_score, cur_score

def solution(dartResult):
    score = [0,0,0]

    for l_idx in range(len(dartResult)):
        l = dartResult[l_idx]
        option = ''

        if l.isdigit():
            if dartResult[l_idx+1].isdigit():
                l = 10
                bonus = dartResult[l_idx+2]
                if l_idx+3 < len(dartResult):
                    option = dartResult[l_idx+3]
            else:
                l = int(l)
                bonus = dartResult[l_idx+1]
                if l_idx+2 < len(dartResult):
                    option = dartResult[l_idx+2]


            if score[0] == 0:
                score[0] = calc_bonus(bonus, l)
                prev, score[0] = calc_option(0, score[0], option)

            elif score[1] == 0:
                score[1] = calc_bonus(bonus, l)
                score[0], score[1] = calc_option(score[0], score[1], option)
            
            else:
                score[2] = calc_bonus(bonus, l)
                if option == '':
                    break
                score[1], score[2] = calc_option(score[1], score[2], option)
    return sum(score)

ss =['1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S','1T2D3D#','1D2S3T*', '2D0D2T*']
for s in ss:
    print(solution(s))