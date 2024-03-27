class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Ordena a lista de números

        result = []  # Inicializa a lista de resultados

        # Itera sobre a lista de números, ignorando os últimos dois elementos
        for i in range(len(nums) - 2):
            # Se o número atual é igual ao anterior, pula para a próxima iteração
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Inicializa dois ponteiros, um no próximo elemento e outro no último elemento da lista
            l, r = i + 1, len(nums) - 1

            # Enquanto o ponteiro esquerdo for menor que o direito
            while l < r:
                # Calcula a soma dos três números
                s = nums[i] + nums[l] + nums[r]

                # Se a soma é menor que zero, move o ponteiro esquerdo para a direita
                if s < 0:
                    l += 1
                # Se a soma é maior que zero, move o ponteiro direito para a esquerda
                elif s > 0:
                    r -= 1
                # Se a soma é igual a zero
                else:
                    # Adiciona a tripla à lista de resultados
                    result.append((nums[i], nums[l], nums[r]))

                    # Enquanto o ponteiro esquerdo for menor que o direito e os números forem iguais, move o ponteiro esquerdo para a direita
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # Enquanto o ponteiro esquerdo for menor que o direito e os números forem iguais, move o ponteiro direito para a esquerda
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # Move ambos os ponteiros
                    l += 1
                    r -= 1

        # Retorna a lista de resultados
        return result
