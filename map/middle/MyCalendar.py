# 我的日程安排表 I
# https://leetcode.cn/problems/my-calendar-i/
from sortedcontainers import SortedDict


class MyCalendar:

    def __init__(self):
        self.map = SortedDict()
        self.map[-2] = -1
        self.map[10 ** 9 + 1] = 10 ** 9 + 2

    def book(self, start: int, end: int) -> bool:
        t = self.map.bisect_left(end)
        if self.map.items()[t - 1][1] <= start:
            self.map[start] = end
            return True
        return False


c = MyCalendar()
assert c.book(10, 20)
assert not c.book(15, 25)
assert c.book(20, 30)