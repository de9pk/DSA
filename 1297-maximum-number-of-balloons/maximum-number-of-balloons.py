class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        freq = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        
        ans = {}
        for i in text:
            ans[i] = ans.get(i, 0) + 1

        b = ans.get('b', 0) // 1
        a = ans.get('a', 0) // 1
        l = ans.get('l', 0) // 2
        o = ans.get('o', 0) // 2
        n = ans.get('n', 0) // 1
        
        
        return min(b, a, l, o, n)