class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        double = []
        
        inicio = 0
        fim = len(numbers) - 1
        
        for i in range(len(numbers)):
            if numbers[inicio] + numbers[fim] == target:
                double = [inicio + 1, fim + 1]
                break
            elif numbers[inicio] + numbers[fim] > target:
                fim -= 1
            else:
                inicio += 1
                
        return double