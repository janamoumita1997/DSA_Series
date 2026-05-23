
def speedtohour(dist,speed):

    hours = 0
    for i in range(len(dist)-1):
        hours += (dist[i] + speed -1)//speed
    hours += dist[-1]/speed

    return hours
    
def minSpeedOnTime(dist, hour):
    if hour <= len(dist) - 1:
        return -1
    left = 0
    right = 10**7
    res = -1

    while left <= right:
        mid = (left + right)//2

        h = speedtohour(dist,mid)
        
        if h <= hour:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    
    hour_ = speedtohour(dist,res)
    if hour_ <= hour:
        return res
    else:
        return -1

dist = [1,1,100000]
dist = [1,3,2]
hour = 2.01
hour = 1.9
print(minSpeedOnTime(dist, hour))