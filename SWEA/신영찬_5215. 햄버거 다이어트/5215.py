'''
접근 방식은
    1. 칼로리당 점수 효율이 높은 순서로 재료들을 나열한다.
    2. 재귀함수를 이용해 모든 경우의 수를 탐색한다.
        재귀함수는 다음과 같이 작동한다.
        input
            1) 재료들의 점수, 칼로리, 칼로리당 점수 배열로 구성된 이중 배열
            2) 여유 칼로리 제한
            3) 누적 점수
        output
            누적 점수
        1. 이중 배열이 빈 배열이면 누적 점수를 바로 리턴한다.
        2. 여유 칼로리 제한이 재료의 칼로리보다 작으면 해당 재료를 포함하지 않은 이중 배열을 다음 재귀함수에 전달한다.
        3. 크다면 해당 재료를 포함 했을 때와 하지 않았을 때로 나눈 누점 점수를 반환 받은 것 중 큰 것을 반환한다.
        4. 같다면 최대 효율이다. 왜냐하면 효율 순으로 정렬했기 때문에 이후 어떤 재료를 많이 넣더라고 같은 칼로리라면 점수를 더 높일 수 없다.
    3. 출력한다.
'''


def food_tree(food_list, L, score):
    if food_list==list():
        return score
    remain = L-food_list[0][1]
    if remain <0:
        return food_tree(food_list[1:],L, score)
    if remain>0:
        ret1=food_tree(food_list[1:],remain,score+food_list[0][0])
        ret2=food_tree(food_list[1:],L,score)
        ret=ret1
        if ret2>ret1:
            ret=ret2
        return ret
    else:
        return score+food_list[0][0]

ts= int(input())
for test_case in range(1,1+ts):
    N, L= list(map(int, input().split()))
    food_list = [ list(map(int, input().split())) for _ in range(N) ]
    for data in food_list:
        data.append(data[0]/data[1])
    for i in range(N-1):
        for j in range(N-1-i):
            if food_list[j][2]<food_list[j+1][2]:
                food_list[j], food_list[j+1]=food_list[j+1], food_list[j]
    score=0
    print('#{} {}'.format(test_case,food_tree(food_list, L, score)))