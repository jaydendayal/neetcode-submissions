class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before = [1] * n
        after = [1] * n
        output = [0] * n

        for i in range (1, n) :
            before[i] = nums[i - 1] * before[i - 1]
        for j in range (n - 2,-1, -1):
            after[j] = nums[j + 1] * after[j + 1]
        for i in range(n):
            output[i] = after[i] * before[i]
        return output

             
            
        