def fib(n: int) -> int:
    if n < 2:
        return n
    prev, curr = 0,1
    for _ in range(2,n+1):
        prev,curr = curr, curr+prev
    return curr

def fib(n: int) -> int:
    if n < 2:
        return n
    prev, curr = 0,1
    for _ in range(2,n+1):
        prev,curr = curr, curr+prev
    return curr

def fact(n):
    if n<2:
        return 1
    res = n*fact(n-1)
    return res
print(fact(5))