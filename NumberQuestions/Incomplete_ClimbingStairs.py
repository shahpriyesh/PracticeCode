class ClimbingStairs:
    def climbingStairs(self, n):
        odd = 0
        if n % 2 != 0:
            odd = 1
            n = n - 1

        pos_2 = (n // 2)
        pos_total = pos_2 + odd
        count = 0

        fact = [0 for i in range(pos_total + 1)]
        fact[0] = 1

        for i in range(1, pos_total + 1):
            fact[i] = i * fact[i-1]

        for idx in range(pos_total + 1):
            count += (fact[pos_total] // (fact[idx] * fact[pos_total - idx]))

        return count


object = ClimbingStairs()
print(object.climbingStairs(2))
print(object.climbingStairs(3))
