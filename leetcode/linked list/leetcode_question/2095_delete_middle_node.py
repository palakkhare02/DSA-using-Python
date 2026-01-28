# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        # Step 1: Count nodes
        temp = head
        N = 0
        while temp:
            N += 1
            temp = temp.next

        # Step 2: Find index before middle
        mid = N // 2

        temp = head
        for _ in range(mid - 1):
            temp = temp.next

        # Step 3: Delete middle
        temp.next = temp.next.next

        return head
