# 1138
# 字母板上的路径

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        x1, y1 = 0, 0
        result = ''
        for c in target:
            x2, y2 = (ord(c) - ord('a')) // 5, (ord(c) - ord('a')) % 5
            if x1 == x2 and y1 == y2:
                result += '!'
                continue
            temp = 'R' * (y2 - y1) if y2 > y1 else 'L' * (y1 - y2)
            temp += 'D' * (x2 - x1) if x2 > x1 else 'U' * (x1 - x2)
            result += temp[::-1] if x1 == 5 else temp
            result += '!'
            x1, y1 = x2, y2
        return result


s = Solution()
assert 'RDD!RRRUU!!DDD!' == s.alphabetBoardPath('leet')
assert 'RR!RRDD!LUU!R!' == s.alphabetBoardPath('code')
assert 'DDDDD!UR!' == s.alphabetBoardPath('zv')
assert 'RDDDD!LD!' == s.alphabetBoardPath('vz')