# fibonacci problem
# write a function fib(n) that takes in a number as an argument.
# the function should return the n-th number of the fib sequence
# fib 1,2,3,4,5,6,7,8,9
# fib 1,1,2,3,5,8,13,21,44
# time = 2^n space = n

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(6))
print(fib(7))
print(fib(8))


# memoization
# hash map
# (keys will be arg to function, value will be the return value)


def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
