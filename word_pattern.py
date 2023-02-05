class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns = {}

        splited = s.split()

        if len(pattern) != len(splited):
            return False

        for i, char in enumerate(pattern):
            if char in patterns and patterns[char] != splited[i]:
                    return False
            else:
                patterns[char] = splited[i]
        
        unique_mapping={value for value in patterns.values()}

        return True if len(unique_mapping) == len(patterns) else False



s = Solution()
print(s.wordPattern(pattern = "abba", s = "dog cat cat dog"))
print(s.wordPattern(pattern = "abba", s = "dog cat cat fish"))
print(s.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
print(s.wordPattern(pattern = "abba", s = "dog dog dog dog"))
