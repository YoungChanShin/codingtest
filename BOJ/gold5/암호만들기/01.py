import sys
sys.stdin = open("input.txt")

L,C = list(map(int,input().split()))
letters = sorted(input().split())
arr=[""]*L

def solution(cnt, depth,mo,ja):
    global L,C
    if depth==L:
        if mo>0 and ja>1:
            print(''.join(arr))
        return

    for i in range(cnt,C):
        arr[depth] = letters[i]
        if "a" == letters[i] or "e" == letters[i] or "i" == letters[i] or "o" == letters[i] or "u" == letters[i]:
            solution(i+1, depth+1,mo+1, ja)
        else:
            solution(i+1, depth+1,mo, ja+1)
            
def myprint(arr):
    for i in arr:
        print(i, end="")
    print()


solution(0,0,0,0)