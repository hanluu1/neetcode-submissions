class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use hash map and pointers for sliding window
        #left pointer start at 0, right start looping through s
        #unseen char will be added in map
        #if find duplicate char
        #we will move left up past the last seen char
        
        #return ans
        ans = 0
        seen = {} #store char as key and last seen index as value
        l = 0
        
        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r #update the new seen index
            ans = max(ans, r - l + 1)
        return ans 
            

