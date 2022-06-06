# 我的日程安排表 III
# https://leetcode.cn/problems/my-calendar-iii/
from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.map = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.map[start] = self.map.setdefault(start, 0) + 1
        self.map[end] = self.map.setdefault(end, 0) - 1
        ans, books = 0, 0
        for value in self.map.values():
            books += value
            ans = max(ans, books)
        return ans


s = MyCalendarThree()
assert s.book(10, 20) == 1
assert s.book(50, 60) == 1
assert s.book(10, 40) == 2
assert s.book(5, 15) == 3
assert s.book(5, 10) == 3
assert s.book(25, 55) == 3