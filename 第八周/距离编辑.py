# 动态规划(分治) 当 str1[i] = str2[j] eidt_distance(i, j) =  eidt_distance(i-1, j-1)
# 当 str1[i] != str2[j] ,eidt_distance(i, j) = min(eidt_distance(i-1, j-1)+1,
# eidt_distance(i, j-1) + 1, eidt_distance(i-1, j) + 1)
import functools
class Solution:
    @functools.lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return len(word1) + len(word2)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = self.minDistance(word1, word2[1:]) + 1
        delate = self.minDistance(word1[1:], word2) + 1
        replace = self.minDistance(word1[1:], word2[1:]) + 1
        return min(insert, delate, replace)
