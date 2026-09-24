class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        pivot = left
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            real_mid = (mid + pivot) % len(nums)
            if (nums[real_mid] == target):
                return real_mid
            elif (target > nums[real_mid]):
                left = mid + 1
            else: 
                right = mid - 1
        return -1
            
