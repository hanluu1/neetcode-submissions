class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #using map to track character return true if second string has the same chars as the first one
        seenS, seenT = {},{}
        if len(s) != len(t):
            return False
        for c in range(len(s)):
            seenS[s[c]] = 1 + seenS.get(s[c],0)
            seenT[t[c]] = 1 + seenT.get(t[c],0)
        return seenS == seenT