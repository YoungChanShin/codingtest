import sys
sys.stdin = open('input.txt')

N = int(input())
# print(ord('A')) = 65
tree=[[] for _ in range(N)]
for _ in range(N):
    root, left, right = list(map(lambda x: ord(x)-65, input().split()))
    tree[root] = [left, right]

def pre(root):
    # print(chr(root))
    print(chr(root+65), end="")
    if tree[root][0]>0:
        pre(tree[root][0]) 
    if tree[root][1]>0:
        pre(tree[root][1]) 
def mid(root):
    # print(chr(root))
    if tree[root][0]>0:
        mid(tree[root][0]) 
    print(chr(root+65), end="")
    if tree[root][1]>0:
        mid(tree[root][1]) 
def post(root):
    # print(chr(root))
    if tree[root][0]>0:
        post(tree[root][0]) 
    if tree[root][1]>0:
        post(tree[root][1]) 
    print(chr(root+65), end="")

pre(0)
print()
mid(0)
print()
post(0)