class Solution:
    # Definindo a classe Solution

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Definindo a função deckRevealedIncreasing que recebe uma lista de inteiros e retorna uma lista de inteiros

        deck.sort()
        # Ordena a lista de entrada em ordem crescente

        res = [0] * len(deck)
        # Cria uma nova lista do mesmo tamanho que a lista de entrada, preenchida com zeros

        q = deque(range(len(deck)))
        # Cria uma deque (uma fila de duas pontas) contendo números de 0 até o tamanho da lista de entrada - 1

        for n in deck:
            # Para cada número na lista de entrada

            i = q.popleft()
            # Remove e retorna o número do início da deque

            res[i] = n
            # Substitui o i-ésimo elemento da lista res pelo número n

            if q:
                # Se ainda houver elementos na deque

                q.append(q.popleft())
                # Remove o número do início da deque e o adiciona ao final

        return res
        # Retorna a lista res