arr = [1,5,10]
k = 1
x = 4

def findKCloset_ele(arr,k,x):
    if x <= arr[0]:
        return arr[:k]
    elif x>=arr[-1]:
        return arr[-k:]
    else:
        left = 0
        right = len(arr) - 1
      
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid

       
        l = left - 1
        r = left
    
        count = 0
        while count < k:
            if l < 0: 
                r += 1
            elif r >= len(arr):
                l -= 1
            if abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else: 
                 r += 1
            count  += 1
      
        return arr[l+1:r]

print(findKCloset_ele(arr,k,x))


