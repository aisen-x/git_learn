class Solution:
    def fib(self, n: int) -> int:
        a = b = 1
        if n == 0 : return 0
        if n == 1 : return 1
        if n == 2 : return 1
        for i in range(3, n+1):
            a, b = b, a + b
        return b

