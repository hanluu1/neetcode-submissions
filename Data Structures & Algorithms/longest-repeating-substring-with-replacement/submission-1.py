class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #only replace at most k letters, and return the longest substring
        #use sliding window 
        # map to access the char and keep track better
        #track how many chars match c 
        #how many replacements needed

        ans = 0
        left = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            while (rigt - left + 1) - max(count.value()) > k:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

           

       