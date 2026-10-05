class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        depth = 0
        
        for i, ch in enumerate(s):
            if ch == "(":
                depth += 1
            else:
                depth -= 1
                # If this ')' directly follows a '(', it's a core unit "()"
                if s[i - 1] == "(":
                    ans += 1 << depth  # Equivalent to 2 ** depth
                    
        return ans