n = 6
p = 2

total_page = 0
if n % 2 == 0:
    total_page = n//2 + 1
else:
    total_page = (n-1)//2 + 1
print('total page : ',total_page)

if p == 1 or p == n:
    print(0)

forward_count = 1
i = 1
while i < n-1:
    if p in [i+1, i+2]:
        break
    else:
        forward_count += 1
    i += 2
back_count = (total_page - 1) - forward_count

print(min(forward_count,back_count))


