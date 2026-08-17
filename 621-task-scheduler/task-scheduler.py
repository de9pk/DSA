import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for ch in tasks:
            freq[ch] = freq.get(ch, 0) + 1

        heap = []

        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch))

        queue = deque()
        time = 0

        while heap or queue:
            time += 1

            if heap:
                count, ch = heapq.heappop(heap)
                count += 1

                if count != 0:
                    queue.append((count, ch, time + n))

            if queue and queue[0][2] == time:
                count, ch, avl = queue.popleft()
                heapq.heappush(heap, (count, ch))

        return time