class SortedSquares:
    def __init__(self):
        pass

    # O(n) time, O(n) space   [ Two Pointer approach ]
    def sortedSquares(self, A):
        result = []
        front = 0
        rear = len(A)-1
        while front <= rear:
            if abs(A[front]) >= abs(A[rear]):
                result.insert(0, A[front] ** 2)
                front += 1
            else:
                result.insert(0, A[rear] ** 2)
                rear -= 1
        return result

    # O(nlgn) time, O(n) space     [ sort approach ]
    def sortedSquares2(self, A):
        result = [n**2 for n in A]
        result.sort()
        return result


object = SortedSquares()
A = [-4,-1,0,3,10]
print(object.sortedSquares2(A))