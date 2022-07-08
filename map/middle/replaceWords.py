# 单词替换
# https://leetcode.cn/problems/replace-words/
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        # 构建字典树
        for map in dictionary:
            temp = trie
            for i in map:
                if i not in temp:
                    temp[i] = {}
                temp = temp[i]
            temp['#'] = {}
        words = sentence.split(' ')

        def getRoot(word: str) -> str:
            root = ''
            t = trie
            for c in word:
                if '#' in t:
                    return root
                if c not in t:
                    return word
                root += c
                t = t[c]
            return root
        return ' '.join([getRoot(word) for word in words])


s = Solution()
assert s.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery") == "the cat was rat by the bat"
assert s.replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs") == "a a b c"
assert s.replaceWords(["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa") == "a a a a a a a a bbb baba a"
