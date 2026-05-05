s = [2,2,1,3,2]
d = 4
m = 2

def birthday(s, d, m):

    if not s:
        return 0
    current_sum = sum(s[:m])
    count = 0

    if current_sum == d:
        count += 1
    for i in range(m,len(s)):
        current_sum += s[i] - s[i-m]
        if current_sum == d:
            count += 1

    return count
