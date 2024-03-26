class Solution:
    def is_twice(self, nums: List[int], num) -> int:
        elements = []
        
        for el in nums:
            if el == num:
                elements.append(el)
        
        return len(elements) == 2
    
    def removeDuplicates(self, nums: List[int]) -> int:
        elements = []
        
        for el in nums:
            if not self.is_twice(elements, el):
                elements.append(el)      
               
        nums = [1] 
        return len(elements)