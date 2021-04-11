class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        res = []
        dict_ = {}
        for i in strs:
            new_i = ''.join(sorted(i))
            if new_i in dict_:
                res[dict_[new_i]].append(i)
            else:
                dict_[new_i] = len(res)
                res.append([i])
        return res