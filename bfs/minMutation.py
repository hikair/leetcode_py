# 最小基因变化
# https://leetcode-cn.com/problems/minimum-genetic-mutation/
from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        bank = set(bank)
        if end not in bank:
            return -1
        q = deque([(start, 0)])
        while q:
            cur, step = q.popleft()
            for i, x in enumerate(cur):
                for y in 'ACGT':
                    if x != y:
                        variant = cur[:i] + y + cur[i + 1:]
                        if variant == end:
                            return step + 1
                        if variant in bank:
                            bank.remove(variant)
                            q.append((variant, step + 1))
        return -1


s = Solution()
# print(s.minMutation('AACCGGTT', 'AACCGGTA', ['AACCGGTA'])) # 1
# print(s.minMutation('AACCGGTT', 'AAACGGTA', ['AACCGGTA', 'AACCGCTA', 'AAACGGTA'])) # 2
print(s.minMutation('AAAAACCC', 'AACCCCCC', ['AAAACCCC', 'AAACCCCC', 'AACCCCCC'])) # 3