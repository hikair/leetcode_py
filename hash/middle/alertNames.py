# 警告一小时内使用相同员工卡大于等于三次的人
# https://leetcode.cn/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/
import collections
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        map = collections.defaultdict(list)
        for name, t in zip(keyName, keyTime):
            t = int(t[:2]) * 60 + int(t[3:])
            map[name].append(t)
        result = []
        for name, ts in map.items():
            if (n := len(ts)) > 2:
                ts.sort()
                for i in range(n - 2):
                    if ts[i + 2] - ts[i] <= 60:
                        result.append(name)
                        break
        result.sort()
        return result


    def alertNames2(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        map = {}

        def convertMinute(keyTime):
            return int(keyTime[0]) * 600 + int(keyTime[1]) * 60 + int(keyTime[3]) * 10 + int(keyTime[4])

        def judge(keyTimes):
            keyTimes.sort()
            queue = collections.deque()
            for keyTime in keyTimes:
                queue.append(keyTime)
                if len(queue) > 1:
                    if keyTime - queue[0] > 60:
                        queue.popleft()
                if len(queue) > 2:
                    return True
            return False

        for i in range(len(keyName)):
            if keyName[i] in map:
                map[keyName[i]].append(convertMinute(keyTime[i]))
            else:
                map[keyName[i]] = [convertMinute(keyTime[i])]
        result = []
        for k in map:
            if judge(map[k]):
                result.append(k)
        result.sort()
        return result


s = Solution()
keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
assert ["daniel"] == s.alertNames(keyName, keyTime)
keyName = ["alice","alice","alice","bob","bob","bob","bob"]
keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
assert ["bob"] == s.alertNames(keyName, keyTime)
keyName = ["john","john","john"]
keyTime = ["23:58","23:59","00:01"]
assert [] == s.alertNames(keyName, keyTime)
keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"]
keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
assert ["clare","leslie"] == s.alertNames(keyName, keyTime)