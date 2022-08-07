# 函数的独占时间
# https://leetcode.cn/problems/exclusive-time-of-functions/
from collections import deque
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        queue, ans = [], [0] * n
        for log in logs:
            arr = log.split(":")
            idx, type, timestamp = int(arr[0]), arr[1], int(arr[2])

            if type == 'start':
                if queue:
                    ans[queue[-1][0]] += timestamp - queue[-1][1]
                    queue[-1][1] = timestamp
                queue.append([idx, timestamp])
            else:
                p = queue.pop()
                ans[p[0]] += timestamp - p[1] + 1
                if queue:
                    queue[-1][1] = timestamp + 1
        return ans


s = Solution()
assert s.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]) == [3, 4]
assert s.exclusiveTime(1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]) == [8]
assert s.exclusiveTime(2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]) == [7, 1]
assert s.exclusiveTime(2, ["0:start:0", "0:start:2", "0:end:5", "1:start:7", "1:end:7", "0:end:8"]) == [8, 1]
assert s.exclusiveTime(1, ["0:start:0", "0:end:0"]) == [1]
