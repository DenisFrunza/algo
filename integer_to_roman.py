class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        roman_values = ("M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I")

        for i, value in enumerate(values):
            while num >= value:
                num -= value
                result.append(roman_values[i])
        
        return "".join(result)


s = Solution()
print(s.intToRoman(252))