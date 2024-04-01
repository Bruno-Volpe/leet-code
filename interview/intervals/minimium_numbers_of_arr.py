class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # A ideia do problema eh acahr o maximo de insterccoes entre os intervalos
        # Isso sera o numero minimo de flechas que voce precisa atirar
        arrows = 0
        
        # Ordenar os intervalos pelo final
        points.sort(key=lambda x: x[1])
        
        for i in range(len(points)):
            if i == 0:
                arrows += 1
                end = points[i][1]
            else:
                if points[i][0] > end:
                    arrows += 1
                    end = points[i][1]
        
        
        return arrows