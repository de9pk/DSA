# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        if head is None:
                return None

        while slow.next is not None:
            if slow.next.val == slow.val:
                slow.next = slow.next.next

            else:
                slow = slow.next

        return head


            
        