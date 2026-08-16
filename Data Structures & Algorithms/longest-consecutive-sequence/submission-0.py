class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longest = 0
        for num in setNums:
            if num - 1 not in setNums:
                count = 1
                i = 1
                while num + i in setNums:
                    count += 1
                    i += 1
                longest = max(longest, count)
        return longest