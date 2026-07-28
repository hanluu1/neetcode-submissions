class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #time = (target - position) / speed
        #pair speed and position together
        pairs = zip(position, speed)
        pairs = sorted(pairs, reverse = True)

        stack = []
        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)
            #if the car behind [-1] have the time less than or equal to the car ahead then it is one fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
                
