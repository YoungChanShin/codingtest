import sys
sys.stdin=open('input.txt')

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, num):
        new_node = Node(num)
        # 큐가 비어 있을 때
        if self.head==None:
            self.head = new_node
        else:
            cur = self.head
            # 데이터가 하나 있을 때
            if cur.next == None:
                if cur.data<num:
                    cur.next = new_node
                else:
                    new_node.next = self.head
                    self.head = new_node
            # 데이터가 둘 이상 있을 때
            else:
                while cur.next.data<num: 
                    cur = cur.next
                    if cur.next == None:
                        break
                    
                if cur == self.head:
                    if cur.data<num:
                        new_node.next = cur.next
                        cur.next = new_node
                    else:
                        new_node.next = self.head
                        self.head = new_node
                else:
                    new_node.next = cur.next
                    cur.next = new_node

    def print(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

N = int(input())
s=Stack()
for _ in range(N):
    s.push(int(input()))
s.print()