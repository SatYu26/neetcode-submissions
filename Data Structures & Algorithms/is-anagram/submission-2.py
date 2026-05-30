class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ms = {}
        n = len(s)
        m = len(t)
        if n != m:
            return False
        for char in s:
            if char in ms:
                ms[char] += 1
            else:
                ms[char] = 1
        for char in t:
            if char in ms and ms[char] >=1 :
                ms[char] -= 1
            else:
                return False
        return True