def combinationSum(candidates, target):
    if not candidates:
        return []
    res = []
    candidates.sort()
    def helper(target, index, sub_list):
        if target == 0:
            res.append(sub_list)
        if target < 0 or index >= len(candidates):
            return
        for i in range(index, len(candidates)):
                #optimization
            if target < candidates[i]:
                break
            helper(target-candidates[i], i, sub_list+[candidates[i]])
    helper(target, 0, [])
    return res


print("Sum of subsets :",combinationSum( [5, 10, 12, 13, 15, 18],30))