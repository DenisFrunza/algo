class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map_one = {}
        map_two = {}

        for i, char in enumerate(s):
            if char in map_one:
                if map_one[char] != t[i]:
                    return False
            else:
                if t[i] in map_two:
                    return False
                else:
                    map_one[char] = t[i]
                    map_two[t[i]] = char
        return True





s = Solution()
print(s.isIsomorphic(s="badc", t="baba"))