class Solution:
    def isValid(self, s: str) -> bool:
        dict = {')': '(', ']':'[', '}':'{'}
        strck = []
        for i in s:
            if strck and i in dict:
                if strck[-1] == dict[i]:strck.pop()
                else:
                    return False
            else:
                strck.append(i)
        return not strck
