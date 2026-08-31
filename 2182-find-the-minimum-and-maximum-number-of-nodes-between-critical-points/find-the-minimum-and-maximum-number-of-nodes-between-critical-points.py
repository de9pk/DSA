class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        prev = head
        curr = head.next
        idx = 1

        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            nxt = curr.next

            if (prev.val < curr.val > nxt.val) or (prev.val > curr.val < nxt.val):

                if first == -1:
                    first = idx
                else:
                    min_dist = min(min_dist, idx - last)

                last = idx

            prev = curr
            curr = nxt
            idx += 1

        if first == -1 or first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]