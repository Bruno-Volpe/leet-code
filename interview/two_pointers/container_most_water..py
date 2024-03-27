# O(N^2)
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         y = 0 
#         x = 0
        
#         max_area = 0
        
#         for i in range(len(height)):
#             for j in range(i+1, len(height)):
#                 if height[i] < height[j]:
#                     y = height[i]
#                 else:
#                     y = height[j]
                
#                 x = j - i
                
#                 if x * y > max_area:
#                     max_area = x * y
        
#         return max_area
    

# O(N)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            area = (right - left) * (height[left] if height[left] < height[right] else height[right])
            if area > max_area:
                max_area = area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area  