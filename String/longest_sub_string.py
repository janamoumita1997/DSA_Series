s = "pwwkew"

q = {}
n = len(s)
left = 0
max_count = 0
for right in range(n):
    while s[right] in q and left <= q[s[right]]<= right:
        left += 1
    q[s[right]] = right
    length = right - left + 1
    max_count = max(max_count,length)
print(max_count)