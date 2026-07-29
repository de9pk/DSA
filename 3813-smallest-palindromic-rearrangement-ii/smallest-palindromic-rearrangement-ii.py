class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter
        import math

        freq = Counter(s)
        half = Counter()
        mid = ""
        m=0

        for ch in sorted(freq):
            half[ch] = freq[ch]//2

            if freq[ch]%2!=0:
                mid+=ch
            
            m+=half[ch]
        
        def get_ways(f,target_k):
            ways=1
            curr_len=0
            for ch in "abcdefghijklmnopqrstuvwxyz":
                count = f.get(ch,0)
                if count>0:
                    curr_len += count
                    ways *= math.comb(curr_len,count)
                    if ways>target_k:
                        return target_k+1
            return ways 

        if get_ways(half,k)<k:
            return ""

        first_half=[]
        for _ in range(m):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if half.get(ch,0)>0:
                    half[ch]-=1
                    ways=get_ways(half,k)

                    if ways>=k:
                        first_half.append(ch)
                        break
                    else:
                        k-=ways
                        half[ch]+=1

        first_str="".join(first_half)
        return first_str+mid+first_str[::-1]   