# https://leetcode.com/problems/first-bad-version/


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:      
    def firstBadVersion(self, n: int) -> int:
        menor = 1
        maior = n
        resultado = n
        while menor <= maior:
            metade = (menor + maior) // 2
            if isBadVersion(metade):
                resultado = metade
                maior = metade - 1
            else:
                menor = metade + 1
        return resultado
