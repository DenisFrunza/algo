class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        hash_table = {}

        for char in s:
            if char in hash_table:
                hash_table[char] += 1
            else:
                hash_table[char] = 1
        
        for char in t:
            if char in hash_table:
                hash_table[char] -= 1
                if hash_table[char] == 0:
                    del hash_table[char]
            else:
                return False
        
        if len(hash_table) >= 1:
            return False
        else:
            return True
