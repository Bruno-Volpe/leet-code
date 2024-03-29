from typing import List

#O(n)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0


# O(n^2)
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         sub_sequences = []
        
#         for i in range(len(nums)):
#             current_sum = 0
#             for j in range(i, len(nums)):
#                 current_sum += nums[j]
#                 if current_sum >= target:
#                     sub_sequences.append(nums[i:j+1])
#                     break  # Se encontrarmos uma soma válida, podemos sair do loop interno
        
#         if not sub_sequences:
#             return 0
        
#         min_length = min(len(sub) for sub in sub_sequences)
#         return min_length
