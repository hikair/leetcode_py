# 实现一个魔法字典
# https://leetcode.cn/problems/implement-magic-dictionary/
from typing import List


class Trie:
    def __init__(self):
        self.is_finish = False
        self.child = {}


class MagicDictionary:

    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            temp = self.root
            for c in word:
                if c not in temp.child:
                    temp.child[c] = Trie()
                temp = temp.child[c]
            temp.is_finish = True

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)

        # limit 必需要修改的次数
        def dfs(node: Trie, pos: int, limit: int):
            if pos == n:
                return node.is_finish and limit == 0
            c = searchWord[pos]
            if c in node.child:
                if dfs(node.child[c], pos + 1, limit):
                    return True
            # 没有次数可以修改了
            if limit == 0:
                return False
            # 尝试消耗一次修改次数
            for i in node.child:
                # 过滤相同的
                if i == c:
                    continue
                if dfs(node.child[i], pos + 1, limit - 1):
                    return True
            return False

        return dfs(self.root, 0, 1)


o = MagicDictionary()
# o.buildDict(["hello", "hallo", "leetcode", "judge", "judgg"])
# print(o.search('judgg'))

o.buildDict(['hello', 'leetcode'])
assert not o.search('hello')
assert o.search('hhllo')
assert not o.search('hell')
assert not o.search('leetcoded')
