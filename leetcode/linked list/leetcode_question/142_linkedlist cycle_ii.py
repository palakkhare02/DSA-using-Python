# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                slow =head
                while slow !=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None            
    

#     🧠 Approach (Floyd’s Cycle Detection)

# Use two pointers slow and fast.

# Move slow by 1 step and fast by 2 steps.

# If they meet, a cycle exists.

# Reset slow to head and move both pointers one step at a time.

# The node where they meet again is the start of the cycle.

# Time Complexity: O(n)
# Space Complexity: O(1)