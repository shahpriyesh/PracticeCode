class MaximumWidthRamp:
    def maximumWidthRamp(self, A):
        pass
        # Following front and rear technique doesn't work
        # front, rear = 0, len(A)-1
        # while front < rear:
        #     if A[front] > A[rear]:
        #         if A[front] <= A[rear-1]:
        #             rear = rear - 1
        #         elif A[front+1] <= A[rear]:
        #             front = front + 1
        #         else:
        #             front = front + 1
        #             rear = rear - 1
        #     else:
        #         return rear - front
        # return 0


object = MaximumWidthRamp()
print(object.maximumWidthRamp([6,0,8,2,1,5]))
print(object.maximumWidthRamp([9,8,1,0,1,9,4,0,4,1]))