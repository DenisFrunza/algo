from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {''.join(sorted(item)): [] for item in strs}

        for item in strs:
            sorted_word = ''.join(sorted(item))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(item)

        return [item for item in anagrams.values()]


s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs=strs))