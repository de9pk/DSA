class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for ch in strs:
            fp = "".join(sorted(ch))

            if fp not in freq:
                freq[fp] = []

            freq[fp].append(ch)

        return list(freq.values())
        


        