class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the intervals
        intervals.sort(key=lambda x : x[0]) #sort by start
        ans = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = ans[-1][1] #the end of the last interval append to the output
            if start <= lastEnd:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])
        return ans