from sys import stdin
stdin = open('input.txt')
read = stdin.readline

num_of_computer = int(read())
computer_link = [[] for _ in range(num_of_computer)]

for _ in range(int(read())):
    c1,c2 = list(map(lambda x: int(x)-1, read().split()))
    computer_link[c1].append(c2)
    computer_link[c2].append(c1)

s = []
visited = []
def search(start):
    visited.append(start)
    s.extend(computer_link[start])
    while len(s)!=0:
        node = s.pop(0)
        if node not in visited:
            search(node)
search(1)
print(len(visited)-1)