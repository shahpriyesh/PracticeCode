class SmallestRange1:
    def smallestRange(self, A, K):
        new_max = max(A) - K
        new_min = min(A) + K

        # check if K is added to min number and K is subtracted from max number,
        #   than does max number become smaller than min number?
        #       In such case, answer is 0
        if new_min >= new_max:
            return 0
        #   does max number remain bigger than min number?
        #       In such case, difference between new max and new min is the answer
        else:
            return new_max - new_min


object = SmallestRange1()
A = [9,9,2,8,7]
K = 4
print(object.smallestRange(A, K))