import math

class CountPrimes:
    def countPrimes(self, n):
        A = [True]*n
        prime_cnt = 0
        end = int(math.sqrt(n)) + 1

        for i in range(2, end):
            if A[i] and self.isPrime(i):
                # strike off all its multiples till n
                x = i
                next = i*x
                while next < n:
                    A[next] = False
                    x += 1
                    next = i*x

        for i in range(2, len(A)):
            if A[i]:
                prime_cnt += 1

        return prime_cnt

    def isPrime(self, x):
        end = int(math.sqrt(x))
        for i in range(2, end):
            if x % i == 0:
                return False
        return True


object = CountPrimes()
print(object.countPrimes(10))