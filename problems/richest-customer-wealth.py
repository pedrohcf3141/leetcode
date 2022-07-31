# https://leetcode.com/problems/richest-customer-wealth/submissions/


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maior = 0
        for account in accounts:
            valor = 0
            for value in account:
                valor += value
            if maior <= valor:
                maior = valor
        return maior
