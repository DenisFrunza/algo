class Solution:
    ROMAN = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    def romanToInt(self, s: str) -> int:
        result = 0
        for i, digit in enumerate(s):
            next = s[i+1] if i+1 < len(s) else None
            match digit:
                case 'I':
                    if next == 'V' or next == 'X':
                        result -= 1
                    else:
                        result += 1
                case 'V':
                    result += 5
                case 'X':
                    if next == 'L' or next == 'C':
                        result -= 10
                    else:
                        result += 10
                case 'L':
                    result += 50
                case 'C':
                    if next == 'D' or next == 'M':
                        result -= 100
                    else:
                        result += 100
                case 'D':
                    result += 500
                case 'M':
                    result += 1000
        return result
s = Solution()

s.romanToInt("MCMXCIV")