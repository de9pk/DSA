import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq={}

        for word in words:
            freq[word]=freq.get(word,0)+1
        
        heap=[]
        heapq.heapify(heap)

        for word,count in freq.items():
            heapq.heappush(heap, (-count,word))

        result=[]
        
        while k:
            count,curr=heapq.heappop(heap)
            result.append(curr)
            k-=1
        
        return result