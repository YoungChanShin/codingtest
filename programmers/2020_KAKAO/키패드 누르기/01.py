def getDistance(start, destination):
    if start in (1,3):
        if destination == 2:
            return 1
        elif destination == 5:
            return 2
        elif destination == 8:
            return 3
        elif destination == 0:
            return 4

    elif start in (4,6):
        if destination in (2, 8):
            return 2
        elif destination == 5:
            return 1
        elif destination == 0:
            return 3

    elif start in (7,9):
        if destination == 2:
            return 3
        elif destination in (0, 5):
            return 2
        elif destination == 8:
            return 1

    elif start in ("*", "#"):
        if destination == 2:
            return 4
        elif destination == 5:
            return 3
        elif destination == 8:
            return 2
        elif destination == 0:
            return 1
    elif start in (2,5,8,0):
        _line = [3,0,0,0,0,1,0,0,2]
        return abs(_line[start] - _line[destination])

def solution(numbers, hand):
    answer = ''
    right = '#'
    left = '*'
    for n in numbers:
        if n in (1,4,7):
            answer += 'L'
            left = n
            continue
        elif n in (3,6,9):
            answer += 'R'
            right = n
            continue
        else:
            right_distance = getDistance(right, n)
            left_distance = getDistance(left, n)

            if right_distance < left_distance:
                answer += 'R'
                right = n
                continue
            elif left_distance < right_distance:
                answer += 'L'
                left = n
                continue
            else:
                if hand == 'left':
                    answer += 'L'
                    left = n
                else:
                    answer += 'R'
                    right = n

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]		
hand = "right"

print(solution(numbers, hand))
result = "LRLLLRLLRRL"