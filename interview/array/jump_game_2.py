class Solution:
    def jump(self, nums: List[int]) -> int:        
        if len(nums) == 1:
            return 0

        for i in range(len(nums), 0, -1):
            if nums[i] == 0:
                return -1
            if nums[i] == 1:
                return len(nums) - i - 1