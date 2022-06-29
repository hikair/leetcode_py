# 质数排列
# https://leetcode.cn/problems/prime-arrangements/

class Solution:

    mod = 1000000007

    def numPrimeArrangements(self, n: int) -> int:
        primes = self.countPrimes(n + 1)
        return self.fact(primes) * self.fact(n - primes) % self.mod

    def countPrimes(self, n: int) -> int:
        arr, sum = [1 for _ in range(n)], 0
        for i in range(2, n):
            if arr[i] == 1:
                sum += 1
                for j in range(i * i, n, i):
                    arr[j] = 0
        return sum

    def fact(self, n: int) -> int:
        ans = 1
        for i in range(2, n + 1):
            ans *= i
        return ans % self.mod


s = Solution()
assert s.numPrimeArrangements(5) == 12
assert s.numPrimeArrangements(100) == 682289015