class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        #how you count the total matches?
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        #implement sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            #return True immediately if it matches at first
            if matches == 26:
                return True

            #calculate matches by adding or subtracting based on the matching 
            #char in the window sliding on s2
            #find the right index
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1 #sliding r index to the right in s2 so add one more
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            #remove left character from window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
            
