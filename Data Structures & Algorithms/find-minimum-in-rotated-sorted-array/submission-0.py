class Solution:
    def findMin(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        return sortedNums[0]
        