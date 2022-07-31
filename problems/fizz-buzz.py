# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        resposta = []
        for x in range(1, n+1):
            nro = x
            if x % 3 == 0:
                nro = "Fizz"
            if x % 5 == 0:
                nro = "Buzz"
            if x % 15 == 0:
                nro = "FizzBuzz"
            resposta.append(str(nro))
        return resposta
