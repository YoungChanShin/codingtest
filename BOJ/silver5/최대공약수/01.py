import sys
import math
sys.stdin = open("input.txt")

num1 , num2 = sorted(list(map(int, input().split())))

gcd=1
lcm=1


start_num = int(math.sqrt(num1))
for i in range(1, start_num+1):
    if num1 % i == 0:
        if num2 % (num1//i) == 0:
            gcd = num1//i
            lcm = num1 * num2//gcd
            break
        if num2 % i == 0:
            gcd = i
            lcm = num1 * num2 //gcd
print(gcd)
print(lcm)