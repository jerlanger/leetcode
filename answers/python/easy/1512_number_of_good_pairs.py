import timeit
import numpy as np

class Solution:

    # init

    def numIdenticalPairs(self, nums: list[int]) -> int:

        ans = []

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    ans.append([i, j])

        return len(ans)

    # revise

    def numIdenticalPairs2(self, nums: list[int]) -> int:

        n = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    n += 1

        return n

    def timing(self, nums: list[int]):

        results = {"Solution 1": np.mean(timeit.repeat(lambda: self.numIdenticalPairs(nums=nums))),
                   "Solution 2": np.mean(timeit.repeat(lambda: self.numIdenticalPairs2(nums=nums)))
                   }

        return results


cases = [[1,2,3,1,1,3],[1,1,1,1],[1,2,3]]
answer = Solution()

for case in cases:
    print(answer.timing(case))

