import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N,M = list(map(int,input().split()))
maps = [list(map(int, input().split())) for _ in range(N)]
