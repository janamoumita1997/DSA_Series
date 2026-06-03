mat = [[10, 3, 15],
        [21, 3, 34],
        [70,  16, 32]]

def find_peak_in_2D(mat):
    n = len(mat)
    m = len(mat[0])

    low = 0
    high = m-1
    mini = -float("inf")
    while low <= high:
        mid = (low + high)//2
        max_row = 0
        for i in range(1,n):
            if mat[i][mid] > mat[max_row][mid]:
                max_row = i
        
        left = mat[max_row][mid-1] if mid>0 else mini
        right = mat[max_row][mid+1] if mid+1<m else mini
        
        if mat[max_row][mid]>= left and mat[max_row][mid]>= right:
            return [max_row,mid]
        elif right >  mat[max_row][mid]:
            low = mid + 1
        else:
            high = mid - 1
    return [-1,-1]

print(find_peak_in_2D(mat))