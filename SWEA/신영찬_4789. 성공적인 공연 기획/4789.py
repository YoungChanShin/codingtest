ts=int(input())
for test_case in range(1,1+ts):
    data_list= list(map(int, list(input().strip())))
    accumulation=[0]*(len(data_list))
    accumulation[0]=data_list[0]
    need_staff=0
    current_clap=accumulation[0]
    for i in range(1,len(data_list)):
        if i>current_clap:
            need_staff+=i-current_clap
        accumulation[i]=accumulation[i-1]+data_list[i]
        current_clap=accumulation[i]+need_staff

    print('#{} {}'.format(test_case, need_staff))

'''
입력값을 data_list에 저장한다.
data_list와 똑같은 크기의 배열 accumulation을 만든다.
이 배열은 해당 인덱스까지 박수를 치고 있는 누적 관객(직원 제외)수를 저장하는 배열이다.
현재 박수를 치고 있는 모든 사람의 수는 accumulation[i]값에 need_staff를 더한 숫자이다.
이 숫자가 인덱스 i보다 작으면 직원수를 부족한 차이만큼 추가한다.
'''