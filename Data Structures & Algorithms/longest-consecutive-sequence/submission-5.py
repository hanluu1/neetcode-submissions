class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Idea: only start counting at the BEGINNING of a streak.
        # 1. Put all numbers in a set so lookups are fast (O(1)).
        # 2. For each number, check if num - 1 is in the set.
        #    - If it is, num is in the middle of a streak, so skip it.
        #    - If it is not, num is the start of a streak, so count upward.
        # 3. Keep the longest streak found and return it.

        res = 0
        seen = set(nums)  # all numbers, for fast lookup

        for num in nums:
            # num - 1 is missing, so num is the start of a streak
            if num - 1 not in seen:
                count = 1  # count num itself

                # keep going while the next number (num + count) exists
                while num + count in seen:
                    count += 1

                # keep the longest streak so far
                res = max(res, count)

        return res