# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        cur = head

        while cur:
            cur = cur.next
            length += 1

        length //= 2
        cur = head
        while length:
            cur = cur.next
            length -= 1

        return cur