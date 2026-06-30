class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #merge overlapping intervals
        #return an array of the non overlapping int cover all the int. in the input 
        
        #assign output
        output = [intervals[0]]
        #sort the intervals by start
        intervals.sort(key = lambda x : x[0])
        #for start and end in intervals
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            #if overlap then return the bigger interval that cover both
            if start <= lastEnd:
                output[-1][1] = max(output[-1][1], end)

            #if not overlap then just append that 2 into output
            else:
                output.append([start, end])
        #return output
        return output