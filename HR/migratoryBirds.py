arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

arr.sort()
print(arr)


max_count = 1
type_count = 1
bird_type = arr[0]

for i in range(1,len(arr)):
    if arr[i-1] == arr[i]:
        type_count += 1
    else:
        type_count = 1
    
    if type_count > max_count:
        bird_type = arr[i]
    max_count = max(max_count,type_count)
print(bird_type)