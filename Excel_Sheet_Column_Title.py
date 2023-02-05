class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            intermediary = chr(ord('A') + (columnNumber-1) % 26)
            result.append(intermediary)
            columnNumber = (columnNumber-1) // 26
        
        result.reverse()
        return ''.join(result)

s = Solution()
print(s.convertToTitle(702))