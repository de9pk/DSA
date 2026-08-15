import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        x=0
        y=0

        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            
            if x==y:
                continue
            else:
                ans=x-y
                heapq.heappush(stones,ans)
        if stones:
            return -stones[0]
        
        return 0

            






