candidates = [2,3,6,7]
target = 7

def combination_sum(candidates, target):
    res = []
    candidates = sorted(list(set(candidates)))

    def backtrack(start:int, _remaining_target:int, path:list)->list:
        if _remaining_target == 0:
            res.append(path.copy())
            return
        if _remaining_target < 0:
            return
        
        for i in range(start,len(candidates)):
            if candidates[i]>_remaining_target:
                break
            path.append(candidates[i])
            backtrack(i,_remaining_target-candidates[i],path)
            path.pop()
    backtrack(0,target,[])
    return res
print(combination_sum(candidates,target))