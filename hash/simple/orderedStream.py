# 1656. 设计有序流
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.elements = [''] * (n + 1)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.elements[idKey] = value
        ans = []
        while self.ptr < len(self.elements):
            if self.elements[self.ptr] == '':
                return ans
            ans.append(self.elements[self.ptr])
            self.ptr += 1
        return ans


s = OrderedStream(5)
assert s.insert(3, 'ccccc') == []
assert s.insert(1, 'aaaaa') == ['aaaaa']
assert s.insert(2, 'bbbbb') == ['bbbbb', 'ccccc']
assert s.insert(5, 'eeeee') == []
assert s.insert(4, 'ddddd') == ['ddddd', 'eeeee']