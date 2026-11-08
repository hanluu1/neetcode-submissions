class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #check if we already see the character
        #using map to track
        #using sliding windows to capture the longest non-repeated substring
        #left shrink in when the repeated char met

        seen = set()
        l = 0
        ans = 0
        
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            ans = max(ans, r - l + 1)
        return ans