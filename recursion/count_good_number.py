import math

n = 5
def pow_2(x,n):
    if n == 0:
        return 1
    res = 1
    while n>0:
        if n%2:
            res *= x
        x = x*x
        n = n//2
    return res
def count_good_number(n):
    mod = 10**9 + 7
    even = math.ceil(n/2)
    odd = n//2

    return (pow_2(5,even) * pow_2(4,odd)) % mod

def power(x,n):
    def helper(x,n):
        if x == 0: return 0
        if n == 0: return 1

        res = helper(x,n//2)
        res = res*res
        return x*res if n%2 else res
    res = helper(x,n)
    return res if n >=0 else 1/res

print(count_good_number(50))


# print(pow_2(5,5))