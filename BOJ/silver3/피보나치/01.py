import sys
sys.stdin = open("input.txt")

iteration_0 = [-1]*41
iteration_1 = [-1]*41

iteration_0[0] = 1
iteration_1[0] = 0

iteration_0[1] = 0
iteration_1[1] = 1

for i in range(2, 41):
    iteration_0[i] = iteration_1[i-1]
    iteration_1[i] = iteration_1[i-1]+iteration_1[i-2]

iteration_0[40] = iteration_1[39]

for _ in range(int(input())):
    N = int(input())
    print(iteration_0[N], iteration_1[N])