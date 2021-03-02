import sys
sys.stdin = open("input.txt")

print(''.join(sorted(list(input()), reverse=True)))


