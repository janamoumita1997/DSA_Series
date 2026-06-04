nums = [[7,1],[2,6],[1,4],[5,2],[10,3],[2,4],[5,9]]
points = [[10,3],[8,10],[2,3],[5,4],[8,5],[7,10],[6,6],[3,6]]
from collections import defaultdict

def find_count(px:int, x_list:list)->int:
    n = len(x_list)
    if n == 1:
        if px <= x_list[0]:
            return 1
        else:
            return 0
    left,right = 0, n-1
    while left <= right:
        mid = (left + right)//2
        if x_list[mid] == px:
            return n-mid
        if x_list[mid]<px:
            left = mid + 1
        else:
            right = mid -1
    count = n - left
    return count


# x_list = [1,2]
# print(find_count(10,x_list))
def rect_count(nums,points):
    height = defaultdict(list)
    for x,y in nums:
        height[y].append(x)

    for i in height:
        height[i].sort()
    print(height)
    res = []
    for px,py in points:
        count = 0
        for i in range(py,101):
            if i in height:
                x_list = height[i]
                count += find_count(px,x_list)
        res.append(count)
    return res

print(rect_count(nums,points))