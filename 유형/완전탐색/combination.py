# n이하의 자연수 중에서 r개의 숫자를 고르는 경우의 수를 모두 구하는 함수 작성
def pick(n, selected, r):
    if r==0:
        print(selected)
    else:
        smallest = 0 if selected==[] else selected[-1]+1
        for next in range(smallest, n):
            selected.append(next)
            pick(n, selected, r-1)
            selected.pop()

# pick(5, [], 3)

from itertools import combinations

print(list(combinations(range(5),3)))