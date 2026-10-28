class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        #sort each word to create a key
        for s in strs:
            key = ''.join(sorted(s))
        
        #group word with the same key
            if key not in group:
                group[key] = []
         
            group[key].append(s)
        return list(group.values())




        

