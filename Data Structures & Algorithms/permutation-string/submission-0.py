class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window
        if len(s1) > len(s2):
            return False
        countS1 = [0] * 26
        countS2 = [0] * 26

        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1
            
        totalMatches = 0
        for i in range(26):
            totalMatches += (1 if countS1[i] == countS2[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if totalMatches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            countS2[index] += 1
            if countS1[index] == countS2[index]:
                totalMatches += 1
            elif countS1[index] + 1 == countS2[index]:
                totalMatches -= 1

            index = ord(s2[l]) - ord('a')
            countS2[index] -= 1
            if countS1[index] == countS2[index]:
                totalMatches += 1
            elif countS1[index] + 1 == countS2[index]:
                totalMatches -= 1
            l+=1
        return totalMatches == 26