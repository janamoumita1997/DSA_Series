low = 200
high = 405
count = 0

if high < 1 or low >high:
    print(0)

i = 0
max_limit_of_3 = 0
while 3**i <= high:
    max_limit_of_3 = i
    i += 1

j = 0
max_limit_of_5 = 0
while 5**j <= high:
    max_limit_of_5 = j
    j += 1

print(max_limit_of_3,max_limit_of_5)

for i in range(max_limit_of_3+1):
    for j in range(max_limit_of_5+1):
        if low <= ((3**i)*(5**j)) <= high:
            count += 1
print(count)