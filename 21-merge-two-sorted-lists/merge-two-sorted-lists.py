# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Anchor for our new list
        dummy = ListNode(0)
        current = dummy
        
        left = list1
        right = list2

        # Instead of i < len(left), check if the current node exists
        while left and right:
            # Your logic: compare values and "append" to the result
            if left.val <= right.val:
                current.next = left
                left = left.next # "i += 1"
            else:
                current.next = right
                right = right.next # "j += 1"
            
            # Move the result pointer forward
            current = current.next

        # "while i < n" equivalent: attach the remaining chain
        if left:
            current.next = left
        if right:
            current.next = right

        # Return the actual head (skipping the dummy)
        return dummy.next
