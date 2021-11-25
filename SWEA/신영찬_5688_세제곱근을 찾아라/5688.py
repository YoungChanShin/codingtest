ts=int(input())
def bin_search(num, start, end):
    a=start
    b=end
    mid=((start+end)//2)
    if mid**3==num:
        return mid
    if mid**3>num:
        end=mid
    else:
        start=mid
    if a==start and b==end:
        return mid
    return bin_search(num, start, end)

for test_case in range(1,1+ts):
    number=int(input())
    ret=bin_search(number, 0,10**6)
    if (ret+1)**3 == number:
        ret=ret+1
    if ret**3 != number:
        ret=-1
    print('#{} {}'.format(test_case, ret))