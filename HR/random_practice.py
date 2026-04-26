# a = [1,2,3]
# b = [3,2,1]
# res = [0,0]
# for i in zip(a,b):
#     if i[0]>i[1]:
#         res[0] += 1
#     elif i[0]<i[1]:
#         res[1] += 1
# print(res)

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    principal_sum = 0
    secondary_sum = 0
    for i in range(n):
        principal_sum += arr[i][i]
        secondary_sum += arr[i][n-i-1]
    res = abs(principal_sum - secondary_sum)
    return res

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def plusMinus(arr):
    # Write your code here
    possitive_count = 0
    negetive_count = 0
    zero_count = 0
    for i in arr:
        if i > 0:
            possitive_count += 1
        elif i < 0:
            negetive_count += 1
        else:
            zero_count += 1
    n = len(arr)
    data = (f"{float(possitive_count/n):.6f}", f"{float(negetive_count/n):.6f}", f"{float(zero_count/n):.6f}")
    result = tuple(float(f"{float(x):.6f}") for x in data)
    return result
    # return (format((possitive_count/n),".6f")), format((negetive_count/n),".6f"), format((zero_count/n),".6f")
arr = [-4, 3, -9, 0, 4, 1]
# print(plusMinus(arr))
# n = 6
# for i in range(1,n+1):
#     print(f"{' '*(n-i)}{"#"*i}")

arr = [73,67,38,33]
for i in arr:
    if i>= 38 and (i%5)>=3:
        print(i + (5-(i%5)))
    else:
        print(i)


