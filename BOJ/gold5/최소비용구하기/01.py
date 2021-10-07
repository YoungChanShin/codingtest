import sys
sys.stdin = open('input.txt')

N = int(input())
M = int(input())
buses = [list(map(int, input().split())) for _ in range(M)]
start, end = list(map(int, input().split()))

