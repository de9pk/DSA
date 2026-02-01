# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)   # Temporary starting node
        tail = dummy           # Pointer to build the result list
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next   # Move tail forward
        
        # Attach remaining nodes (only one list will have nodes left)
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next
