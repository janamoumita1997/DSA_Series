chars = ["a","a","b","b","c","c","c"]

# res = ''
# count = 1

# for i in range(1,len(chars)):
#     if chars[i] == chars[i-1]:
#         count += 1
#     else:
#         chars[i-1]= str(count) if count > 1
#         count = 1
# res += chars[-1] + str(count) if count > 1 else chars[-1]

# print(len(res))


chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

i,j = 0,0
n = len(chars)
while i < n:
    current_char = chars[i]
    count = 0
    while i < n and chars[i] == current_char:
        i += 1
        count += 1
    chars[j] = current_char
    j += 1

    if count > 1:
        for digit in str(count):
            chars[j] = digit
            j += 1
print(j)
print(chars)