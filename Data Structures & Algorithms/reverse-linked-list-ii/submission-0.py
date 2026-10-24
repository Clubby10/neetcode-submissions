# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy

        for _ in range(left - 1):
            before = before.next

        tail = before.next

        for _ in range(right - left):
            moving = tail.next
            tail.next = moving.next 
            moving.next = before.next
            before.next = moving



        return dummy.next