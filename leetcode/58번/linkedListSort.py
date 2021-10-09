# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, front, back):
        if front and back:
            if front.val > back.val:
                front, back = back, front
            front.next = self.mergeTwoLists(front.next, back)
        return front or back

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # Runner 기법 - LinkedList에서 전체 크기를 모르는 상태에서 절반인 지점을 찾기 위한 기법
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = (
                slow,
                slow.next,
                fast.next.next,
            )  # slow가 한칸씩 이동하는 동안 fast는 두칸씩 이동
        half.next = None

        # 분할 재귀 호출
        front = self.sortList(head)
        back = self.sortList(slow)

        return self.mergeTwoLists(front, back)