class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Sliding window 3 pointers
        left_far = 0
        left_close = 0
        k = 0
        
        hash_map = defaultdict(int)
        
        for right in range(len(nums)):
            hash_map[nums[right]] += 1
            
            while len(hash_map) > k:
                hash_map[nums[left_close]] -= 1
                if hash_map[nums[left_close]] == 0:
                    hash_map.pop(nums[left_close])
                left_close += 1
                left_far = left_close

            while hash_map[nums[left_close]] > 1:
                hash_map[nums[left_close]] -= 1
                left_close += 1
            
            if len(hash_map) == k:
                k += left_close - left_far + 1
        return k