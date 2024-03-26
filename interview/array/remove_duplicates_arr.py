class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Se a lista tem menos de 3 elementos, não há como ter 3 duplicatas
        if len(nums) < 3:
            return len(nums)
        
        # Inicializa o ponteiro 'slow' em 2, pois os dois primeiros elementos não podem ser duplicatas
        slow = 2

        # Itera sobre a lista a partir do terceiro elemento
        for fast in range(2, len(nums)):
            # Se o elemento atual (fast) é diferente dos dois anteriores
            if nums[fast] != nums[slow - 2]:
                # Move o elemento atual para a posição do ponteiro 'slow'
                nums[slow] = nums[fast]
                # Avança o ponteiro 'slow'
                slow += 1
                
        # Retorna a posição do ponteiro 'slow', que é a quantidade de elementos sem duplicatas
        return slow
