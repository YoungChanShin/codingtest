ts= int(input())
for test_case in range(1,1+ts):
    N, Q=list(map(int, input().split()))
    data_list=[0]*N
    for i in range(1,1+Q):
        start, end= list(map(int, input().split()))
        for idx in range(start, end+1):
            data_list[idx-1]=i
    print('#'+str(test_case), end=' ')
    print(*data_list)