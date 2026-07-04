class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                #get ascii number of current char - to the first char to map the char to index
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s) #count of each char is the key, use tuple in python
        return list(ans.values())

