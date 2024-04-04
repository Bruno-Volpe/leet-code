# class Solution:
#     def maxDepth(self, s: str) -> int:
#         max_count = 0
#         s_arr = list(s)
        
#         for i in range(len(s_arr)):
#             conut = 0
#             for j in range(i - 1, -1, -1):
#                 if s_arr[j] == '(':
#                     conut += 1    
#                 elif s_arr[j] == ')':
#                     conut -= 1    
                                
#             if conut > max_count:
#                 max_count = conut
                    
#         return max_count

class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        current_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
                
        return max_depth
