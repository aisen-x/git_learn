from typing import List
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank: return -1
        dict_ = {
            "A": "CGT",
            "C": "AGT",
            "G": "CAT",
            "T": "CGA"
        }
        queue = [(start, 0)]
        while queue:
            node, step = queue.pop(0)
            if node == end:
                return step
            for i, s in enumerate(node):
                for c in dict_[s]:
                    new = node[:i] + c + node[i+1:]
                    if new in bank:
                        queue.append((new, step+1))
                        bank.remove(new)
        return -1