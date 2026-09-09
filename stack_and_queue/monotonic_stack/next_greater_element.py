nums2 = [1,2,3,4]
nums1 = [2,4]

def getNextGreaterElement(nums1, nums2):
    n2 = len(nums2)
    n1 = len(nums1)
    if n1 == 0 or n2 == 0:
        return []
    stack = []
    lst = [-1]*n2
    final_lst = [-1]*n1

    for i in range(n2-1,-1,-1):

        while len(stack)>0 and nums2[i] > stack[-1]:
            stack.pop()

        if stack:
            lst[i] = stack[-1]

        stack.append(nums2[i])


    nums2_pos = {}
    for k,v in enumerate(nums2):
        nums2_pos[v] = k
    nums12nums2 = {}
    for i,j in enumerate(nums1):
        nums12nums2[i] = nums2_pos[j]



    for i in range(n1):
        final_lst[i] = lst[nums12nums2[i]]

    return final_lst