from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(remainder, path, index):
            if remainder == 0:
                combos.append(path)
            if remainder < 0:
                return
            currval = candidates[index]
            path.append(currval)
            backtrack(remainder-currval, path, index+1)
            path.pop()
            backtrack(remainder, path, index+1)

        combos = []
        backtrack(target, [], 0)
        return combos