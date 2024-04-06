class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        
        for i in range(len(nums)):
            nums[i], mult = mult, mult * nums[i:len(nums)]            
            
            
        return nums