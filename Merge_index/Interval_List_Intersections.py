"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
"""
firstList = [[1,3],[5,9]]
secondList = []


overlap = []
n = len(secondList)
for i in range(n):
    if firstList[i][0] <= secondList[i][0] <= secondList[i][1]:
        overlap.append([secondList[i][0],firstList[i][1]])
    if i < n-1 and secondList[i][1] == firstList[i+1][0]:
        overlap.append([secondList[i][1],secondList[i][1]])
print(overlap)
