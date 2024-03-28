class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        hash_map = defaultdict(int)
        left = 0

        for right in range(len(nums)):
            hash_map[nums[right]] += 1
            
            while hash_map[nums[right]] > k:
                hash_map[nums[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        
        return res