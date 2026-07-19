from collections import Counter

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        seen = set()
        stack = []
        
        for ch in s:
            # 1. Skip immediately if already in the stack
            if ch in seen:
                freq[ch] -= 1  # Decrement before skipping so the count remains accurate
                continue
            
            # 2. Monotonic check: pop if top is larger AND appears again later
            # (freq[stack[-1]] > 0 means it still exists later in the string)
            while stack and stack[-1] > ch and freq[stack[-1]] > 0:
                seen.remove(stack.pop())

            # 3. Add current character to stack and seen set
            stack.append(ch)
            seen.add(ch)
            
            # 4. Successfully processed this instance of the character
            freq[ch] -= 1

        return "".join(stack)
