class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = {}
        for i in s:
            if i in l:
                l[i] += 1
            else:
                l[i] = 1
        for idx, ch in enumerate(s):
            if l[ch] == 1:
                return idx
        
        return -1   