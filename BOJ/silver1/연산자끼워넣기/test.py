import sys

arr = [1,2,3,4,5]

def perm(arr,cnt,ret,checkList):
    if cnt == len(arr):
        print(ret)
        return
    for i in range(len(arr)):
        if checkList[i]==0:
            checkList[i] = 1
            perm(arr, cnt+1, ret+str(arr[i]), checkList)
            checkList[i] = 0

checkList = [0]*len(arr)
perm(arr, 0, "", checkList)

print(arr+[9])