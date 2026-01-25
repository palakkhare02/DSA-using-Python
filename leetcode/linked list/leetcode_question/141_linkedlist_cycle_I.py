# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
              return True

        return False      
    
# 🧠 Approach (Detect Cycle)

# Use two pointers slow and fast.

# Move slow one step and fast two steps.

# If they ever meet, a cycle exists → return True.

# If fast reaches None, no cycle exists → return False.

# Time Complexity: O(n)
# Space Complexity: O(1)