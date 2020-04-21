class FibonacciNumber:
    def fibonacci(self, N):
        store = [0] * (N + 2)
        store[1] = 1

        def fib(N, store):
            if N == 0:
                return store[0]
            if N == 1:
                return store[1]
            if store[N]:
                return store[N]
            store[N] = fib(N-1, store) + fib(N-2, store)
            return store[N]

        return fib(N, store)


object = FibonacciNumber()
print(object.fibonacci(0))
print(object.fibonacci(2))
print(object.fibonacci(3))
print(object.fibonacci(4))