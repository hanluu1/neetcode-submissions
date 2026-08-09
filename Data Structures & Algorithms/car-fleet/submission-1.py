class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # s = v*t -> t = s/v = (target - pos) / speed
        #create array of pair
        pair = zip(position, speed)
        pair = sorted(pair, reverse = True)

        stack = []
        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
