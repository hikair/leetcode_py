class Solution:
    def romanToInt(self, s):
        map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        size = len(s)
        num = 0
        for index,str in enumerate(s):
            sign = 1
            if index + 1 < size:
                if map[str] < map[s[index+1]]:
                    sign = -1
            num += map[str] * sign
        return num
s = Solution()
result = s.romanToInt('III') # 3
print(result)
result = s.romanToInt('IV') # 4
print(result)
result = s.romanToInt('IX') # 9
print(result)
result = s.romanToInt('LVIII') # 58
print(result)
result = s.romanToInt('MCMXCIV') # 1994
print(result)