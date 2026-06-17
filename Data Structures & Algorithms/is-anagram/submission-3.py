class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #did 2 way one is sorted array then compare, 2nd is using hashmap
        #hash map to store char in s then loop through t 
        #if chars from t in s then return true else false
        charS = {}
        charT = {}
        if len(s) != len(t):
            return False
        for c in range(len(s)):
            charS[s[c]] = 1 + charS.get(s[c],0)
            charT[t[c]] = 1 + charT.get(t[c],0)
        return charS == charT