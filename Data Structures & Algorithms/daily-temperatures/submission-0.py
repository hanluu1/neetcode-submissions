class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #return the array of days befor the day that have warmer temp than the current day
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result