class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Esta função mistura duas listas de números, nums1 e nums2.
        """
        # Enquanto ainda houver números em ambas as listas
        while m > 0 and n > 0:
            # Se o último número em nums1 for maior ou igual ao último em nums2
            if nums1[m-1] >= nums2[n-1]:
                # Coloque esse número no final da lista combinada
                nums1[m+n-1] = nums1[m-1]
                # E então nós "removemos" esse número de nums1
                m -= 1
            else:
                # Se o último número em nums2 for maior, faça a mesma coisa, mas com nums2
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        # Se ainda houver números em nums2 depois de nums1 estar vazio
        if n > 0:
            # Coloque o restante de nums2 no início da lista combinada
            nums1[:n] = nums2[:n]