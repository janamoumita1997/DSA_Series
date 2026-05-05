# ar = [5,9,10,7,4]
ar = [1,3,2,6,1,2]
# k = 2
k = 3
count = 0

seen_lst = {}
for i in ar:
    x = (k - (i % k))%k
    if x in seen_lst:
        count += seen_lst[x]
    seen_lst[i % k] = seen_lst.get(i % k,0) + 1
print(count)

count = 0
remainder_map = {}

for num in ar:
    rem = num % k
    # complement remainder needed to make sum divisible by k
    complement = (k - rem) % k
    # if complement exists in map, add its frequency
    count += remainder_map.get(complement, 0)
    # store current remainder
    remainder_map[rem] = remainder_map.get(rem, 0) + 1

print(count)
