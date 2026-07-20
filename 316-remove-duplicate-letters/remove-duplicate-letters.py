class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)
        seen =set()
        stack = []

        for ch in s:
            freq[ch]-=1
            if ch not in seen:
                while stack and stack[-1]>ch and freq[stack[-1]]>0:
                    pc = stack.pop()
                    seen.remove(pc)
                stack.append(ch)
                seen.add(ch)

        return "".join(stack)