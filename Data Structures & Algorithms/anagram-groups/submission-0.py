class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hash save key
        ans = defaultdict(list)
        for s in strs:
            count = [0]* 26 #26 characters map index a to zero
            for i in s:
                count[ord(i) - ord('a')] +=1 #map index to each number by get ascii number of letter minus to ascii a because a is a start number
            #group all anagram by count 
            ans[tuple(count)].append(s) 
        return list(ans.values())
        